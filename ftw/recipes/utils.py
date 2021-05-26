from typing import Any, Dict, List, Optional
import pandas as pd
from ..metadata.utils import UserMetadata
from ..timeline.utils import UserTimeline
from ..metadata import get_all_metadata_features
from ..timeline import get_all_timeline_features
from ..text_features.features import get_all_text_features
from ..distribution import get_distributon_features
from ..likelihood import get_all_ngram_loglikelihood_features


def get_metadata_features_small(
    metadata: Optional[UserMetadata] = None,
    metadata_features: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    feature_lst = [
        "metadata.metadata_features.statuses_count",
        "metadata.metadata_features.favourites_count",
        "metadata.metadata_features.followers_count",
        "metadata.metadata_features.friends_count",
        "metadata.metadata_features.listed_count",
        "metadata.metadata_features.is_default_profile",
        "metadata.metadata_features.is_profile_use_background_image",
        "metadata.metadata_features.is_verified",
        "metadata.metadata_features.tweet_freq",
        "metadata.metadata_features.favourites_growth_rate",
        "metadata.metadata_features.followers_growth_rate",
        "metadata.metadata_features.friends_growth_rate",
        "metadata.metadata_features.listed_growth_rate",
        "metadata.metadata_features.followers_friends_ratio",
        "metadata.metadata_features.description_length",
        "metadata.metadata_features.name_length",
        "metadata.metadata_features.screen_name_length",
        "metadata.metadata_features.num_digits_in_name",
        "metadata.metadata_features.num_digits_in_screen_name",
        "metadata.metadata_likelihood_features.screen_name.2",
    ]

    if metadata_features is None:
        metadata_features = construct_metadata_features(metadata, is_text_features=True, is_likelihood_features=True)
        metadata_features = flatten_dict(metadata_features, ".")

    metadata_features_small = {
        k: metadata_features[k]
        for k in feature_lst
    }

    return metadata_features_small


def construct_metadata_features(
    metadata: Optional[UserMetadata],
    is_text_features: bool = True,
    is_likelihood_features: bool = True,
) -> Dict[str, Any]:
    if metadata is not None:
        metadata_features = get_all_metadata_features(metadata)
    else:
        metadata_features = {}

    if is_text_features:
        metadata_text_features = get_metadata_text_features(metadata)
    else:
        metadata_text_features = {}

    if is_likelihood_features:
        metadata_likelihood_features = get_metadata_likelihood_features(metadata)
    else:
        metadata_likelihood_features = {}

    return {
        "metadata_features": metadata_features,
        "metadata_text_features": metadata_text_features,
        "metadata_likelihood_features": metadata_likelihood_features,
    }


def construct_multiple_metadatas_features(
    metadatas: List[UserMetadata],
    is_text_features: bool = True,
    is_likelihood_features: bool = True,
    is_distribution_features: bool = True,
    is_text_distribution_features: bool = True,
) -> Dict[str, Any]:
    if len(metadatas) == 0:
        return construct_metadata_features(metadata=None, is_text_features=is_text_features, is_likelihood_features=is_likelihood_features)
    elif len(metadatas) == 1:
        return construct_metadata_features(metadata=metadatas[0], is_text_features=is_text_features, is_likelihood_features=is_likelihood_features)
    else:
        metadatas = sorted(metadatas, reverse=True, key=lambda x: x.probe_time)
        multiple_metadatas_features = {
            i: construct_metadata_features(
                metadata,
                is_text_features=is_text_features or is_text_distribution_features,
                is_likelihood_features=is_likelihood_features,
            )
            for i, metadata in enumerate(metadatas)
        }

        last_metadata_features_all = multiple_metadatas_features.get(0, {})
        last_metadata_features = last_metadata_features_all["metadata_features"]
        if is_text_features:
            last_metadata_text_features = last_metadata_features_all["metadata_text_features"]
        else:
            last_metadata_text_features = {}
        
        if is_distribution_features:
            keys = list(last_metadata_features_all["metadata_features"].keys())

            multiple_metadatas_distribution_features = {
                key: get_distributon_features([value["metadata_features"][key] for value in multiple_metadatas_features.values()], value_type=None)
                for key in keys
            }
        else:
            multiple_metadatas_distribution_features = {}
        
        if is_text_distribution_features:
            keys = list(last_metadata_features_all["metadata_text_features"].keys())

            multiple_metadatas_text_distribution_features = {
                key: get_distributon_features([value["metadata_text_features"][key] for value in multiple_metadatas_features.values()], value_type=None)
                for key in keys
            }
        else:
            multiple_metadatas_text_distribution_features = {}


    return {
        "last_metadata_features": last_metadata_features,
        "last_metadata_text_features": last_metadata_text_features,
        "multiple_metadatas_distribution_features": multiple_metadatas_distribution_features,
        "multiple_metadatas_text_distribution_features": multiple_metadatas_text_distribution_features,
    }


def construct_timeline_features(
    timeline: Optional[UserTimeline],
    is_text_features: bool = True,
    is_distribution_features: bool = True,
    is_text_distribution_features: bool = True,
) -> Dict[str, Any]:
    if timeline is not None:
        timeline_features = get_all_timeline_features(timeline)
    else:
        timeline_features = {}

    if is_text_features:
        timeline_text_features = get_timeline_text_features(timeline)
    else:
        timeline_text_features = {}

    if is_distribution_features:
        timeline_distribution_features = get_timeline_distribution_features(timeline)
    else:
        timeline_distribution_features = {}
    
    if is_text_distribution_features:
        timeline_text_distribution_features = get_timeline_text_distribution_features(timeline, timeline_text_features)
    else:
        timeline_text_distribution_features = {}

    return {
        "timeline_features": timeline_features,
        "timeline_text_features": timeline_text_features,
        "timeline_distribution_features": timeline_distribution_features,
        "timeline_text_distribution_features": timeline_text_distribution_features,
    }


def get_metadata_text_features(metadata: Optional[UserMetadata]) -> Dict[str, Any]:
    keys = ["screen_name", "description", "name"]

    if metadata is not None:
        metadata_text_features = {
            key: get_all_text_features(metadata.get_usermetadata_attr(key, ""), pos=True, sentiment=True, word_dims=None, verbose=False)
            for key in keys
        }
    else:
        metadata_text_features = {}

    return metadata_text_features


def get_metadata_likelihood_features(metadata: Optional[UserMetadata]) -> Dict[str, Any]:
    keys = ["screen_name"]

    if metadata is not None:
        metadata_likelihood_features = {
            key: get_all_ngram_loglikelihood_features(text=metadata.get_usermetadata_attr(key, ""), col_name=key, order=2)
            for key in keys
        }
    else:
        metadata_likelihood_features = {}

    return metadata_likelihood_features


def get_timeline_text_features(timeline: Optional[UserTimeline]) -> Dict[str, Any]:
    keys = ["all_tweet_texts", "ordinary_tweet_texts", "retweet_tweet_texts", "quote_tweet_texts", "mention_tweet_texts"]

    if timeline is not None:
        timeline_text_features = {
            key: {
                i: get_all_text_features(el, pos=True, sentiment=True, word_dims=None, verbose=False)
                for i, el in enumerate(timeline.get_tweet_attr(key, ""))
            }
            for key in keys
        }
    else:
        timeline_text_features = {}

    return timeline_text_features


def get_timeline_distribution_features(timeline: Optional[UserTimeline]) -> Dict[str, Any]:
    distribution_keys = {
        "tweet_types": "categorical",
        "tweet_sources": "categorical",
        "tweet_places": "categorical",
        "tweet_filter_levels": "categorical",
        "tweet_langs": "categorical",
        "all_tweet_time_differences": "numerical",
        "ordinary_tweet_time_differences": "numerical",
        "retweet_tweet_time_differences": "numerical",
        "quote_tweet_time_differences": "numerical",
        "mention_tweet_time_differences": "numerical",
        "tweet_has_coordinates": "boolean",
        "tweet_is_possibly_sensitive": "boolean",
        "tweet_is_withheld_copyright": "boolean",
        "tweet_withheld_in_countries_count": "numerical",
        "tweet_quote_counts": "numerical",
        "tweet_reply_counts": "numerical",
        "tweet_retweet_counts": "numerical",
        "tweet_favorite_counts": "numerical",
        "tweet_hashtags_in_entities_counts": "numerical",
        "tweet_urls_in_entities_counts": "numerical",
        "tweet_user_mentions_in_entities_counts": "numerical",
        "tweet_media_in_entities_counts": "numerical",
        "tweet_symbols_in_entities_counts": "numerical",
        "tweet_polls_in_entities_counts": "numerical",
    }

    if timeline is not None:
        timeline_distribution_features = {
            key: get_distributon_features(timeline.get_tweet_attr(key, None), value_type)
            for key, value_type in distribution_keys.items()
        }
    else:
        timeline_distribution_features = {}

    return timeline_distribution_features


def get_timeline_text_distribution_features(
    timeline: Optional[UserTimeline],
    timeline_text_features: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    if timeline_text_features is None:
        timeline_text_features = get_timeline_text_features(timeline)

    timeline_text_distribution_features = {
        key: get_distributon_features(list(timeline_text_feature.values()), value_type=None)
        for key, timeline_text_feature in timeline_text_features.items()
    }

    return timeline_text_distribution_features


def flatten_dict(dct: Dict[str, Any], seperator: str = ".") -> Dict[str, Any]:
    df = pd.json_normalize(dct, sep=seperator)
    return df.to_dict(orient="records")[0]
