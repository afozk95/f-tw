from typing import Any, Dict, List, Optional
from ..metadata.utils import UserMetadata
from ..timeline.utils import UserTimeline
from .utils import (
    construct_metadata_features,
    construct_multiple_metadatas_features,
    construct_timeline_features,
    flatten_dict,
)


def get_features_classical(
    metadata: Optional[UserMetadata] = None,
    timeline: Optional[UserTimeline] = None,
    flatten_separator: Optional[str] = None,
) -> Dict[str, Any]:
    metadata_features = construct_metadata_features(metadata, is_text_features=True, is_likelihood_features=True)
    timeline_features = construct_timeline_features(timeline, is_text_features=True, is_distribution_features=True, is_text_distribution_features=True)

    features = {
        "metadata": metadata_features,
        "timeline": timeline_features,
    }

    if flatten_dict is None:
        return features
    else:
        return flatten_dict(features, flatten_separator)


def get_features_multiple_metadatas(
    metadatas: List[UserMetadata] = [],
    timeline: Optional[UserTimeline] = None,
    flatten_separator: Optional[str] = None,
) -> Dict[str, Any]:
    multiple_metadatas_features = construct_multiple_metadatas_features(metadatas, is_text_features=True, is_distribution_features=True, is_text_distribution_features=True)
    timeline_features = construct_timeline_features(timeline, is_text_features=True, is_distribution_features=True, is_text_distribution_features=True)

    features = {
        "metadatas": multiple_metadatas_features,
        "timeline": timeline_features,
    }

    if flatten_dict is None:
        return features
    else:
        return flatten_dict(features, flatten_separator)


# TODO
def get_features_stream(
    metadatas: List[UserMetadata] = [],
    timeline: Optional[UserTimeline] = None,
    flatten_separator: Optional[str] = None,
) -> Dict[str, Any]:
    metadata_features = construct_metadata_features(metadata)
    timeline_features = construct_timeline_features(timeline)

    features = {
        "metadata_features": metadata_features,
        "timeline_features": timeline_features,
    }

    if flatten_dict is None:
        return features
    else:
        return flatten_dict(features, flatten_separator)