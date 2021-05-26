from typing import List, Optional
from .utils import (
    UserTimeline,
    get_tweet_time_differences_in_sec,
)


def f_tweet_types(timeline: UserTimeline) -> List[str]:
    return [timeline.get_tweet_type(tweet) for tweet in timeline.user_timeline]


def f_tweet_sources(timeline: UserTimeline) -> List[Optional[str]]:
    return timeline.get_tweet_attr("source", None)


def f_tweet_places(timeline: UserTimeline) -> List[Optional[str]]:
    return [place.get("id", None) for place in timeline.get_tweet_attr("place", {})]


def f_tweet_filter_levels(timeline: UserTimeline) -> List[Optional[str]]:
    return timeline.get_tweet_attr("filter_level", None)


def f_tweet_langs(timeline: UserTimeline) -> List[Optional[str]]:
    return timeline.get_tweet_attr("lang", None)


def f_all_tweet_time_differences(timeline: UserTimeline) -> List[float]:
    tweet_objs = timeline.get_all_tweets()
    tweet_created_ats = timeline.get_tweet_attr("created_at", None, tweets=tweet_objs)
    return get_tweet_time_differences_in_sec(tweet_created_ats)


def f_ordinary_tweet_time_differences(timeline: UserTimeline) -> List[float]:
    tweet_objs = timeline.get_ordinary_tweets()
    tweet_created_ats = timeline.get_tweet_attr("created_at", None, tweets=tweet_objs)
    return get_tweet_time_differences_in_sec(tweet_created_ats)


def f_retweet_tweet_time_differences(timeline: UserTimeline) -> List[float]:
    tweet_objs = timeline.get_retweet_tweets()
    tweet_created_ats = timeline.get_tweet_attr("created_at", None, tweets=tweet_objs)
    return get_tweet_time_differences_in_sec(tweet_created_ats)


def f_quote_tweet_time_differences(timeline: UserTimeline) -> List[float]:
    tweet_objs = timeline.get_quote_tweets()
    tweet_created_ats = timeline.get_tweet_attr("created_at", None, tweets=tweet_objs)
    return get_tweet_time_differences_in_sec(tweet_created_ats)


def f_mention_tweet_time_differences(timeline: UserTimeline) -> List[float]:
    tweet_objs = timeline.get_mention_tweets()
    tweet_created_ats = timeline.get_tweet_attr("created_at", None, tweets=tweet_objs)
    return get_tweet_time_differences_in_sec(tweet_created_ats)


def f_all_tweet_texts(timeline: UserTimeline) -> List[str]:
    tweet_objs = timeline.get_all_tweets()
    return timeline.get_tweet_attr("text", "", tweets=tweet_objs)


def f_ordinary_tweet_texts(timeline: UserTimeline) -> List[str]:
    tweet_objs = timeline.get_ordinary_tweets()
    return timeline.get_tweet_attr("text", "", tweets=tweet_objs)


def f_retweet_tweet_texts(timeline: UserTimeline) -> List[str]:
    tweet_objs = timeline.get_retweet_tweets()
    return timeline.get_tweet_attr("text", "", tweets=tweet_objs)


def f_quote_tweet_texts(timeline: UserTimeline) -> List[str]:
    tweet_objs = timeline.get_quote_tweets()
    return timeline.get_tweet_attr("text", "", tweets=tweet_objs)


def f_mention_tweet_texts(timeline: UserTimeline) -> List[str]:
    tweet_objs = timeline.get_mention_tweets()
    return timeline.get_tweet_attr("text", "", tweets=tweet_objs)


def f_tweet_has_coordinates(timeline: UserTimeline) -> List[bool]:
    return [el is not None for el in timeline.get_tweet_attr("coordinates", None)]


def f_tweet_is_possibly_sensitive(timeline: UserTimeline) -> List[str]:
    return timeline.get_tweet_attr("possibly_sensitive", None)


def f_tweet_is_withheld_copyright(timeline: UserTimeline) -> List[str]:
    return timeline.get_tweet_attr("withheld_copyright", None)


def f_tweet_withheld_in_countries_count(timeline: UserTimeline) -> List[str]:
    return [len(el) if isinstance(el, list) else None for el in timeline.get_tweet_attr("withheld_in_countries", None)]


def f_tweet_quote_counts(timeline: UserTimeline) -> List[int]:
    return timeline.get_tweet_attr("quote_count", 0)


def f_tweet_reply_counts(timeline: UserTimeline) -> List[int]:
    return timeline.get_tweet_attr("reply_count", 0)


def f_tweet_retweet_counts(timeline: UserTimeline) -> List[int]:
    return timeline.get_tweet_attr("retweet_count", 0)


def f_tweet_favorite_counts(timeline: UserTimeline) -> List[int]:
    return timeline.get_tweet_attr("favorite_count", 0)


def f_tweet_hashtags_in_entities_counts(timeline: UserTimeline) -> List[int]:
    all_entities = timeline.get_tweet_attr("entities", {})
    return [len(entities["hashtags"]) for entities in all_entities]


def f_tweet_urls_in_entities_counts(timeline: UserTimeline) -> List[int]:
    all_entities = timeline.get_tweet_attr("entities", {})
    return [len(entities["urls"]) for entities in all_entities]


def f_tweet_user_mentions_in_entities_counts(timeline: UserTimeline) -> List[int]:
    all_entities = timeline.get_tweet_attr("entities", {})
    return [len(entities["user_mentions"]) for entities in all_entities]


def f_tweet_media_in_entities_counts(timeline: UserTimeline) -> List[int]:
    all_entities = timeline.get_tweet_attr("entities", {})
    return [len(entities["media"]) for entities in all_entities]


def f_tweet_symbols_in_entities_counts(timeline: UserTimeline) -> List[int]:
    all_entities = timeline.get_tweet_attr("entities", {})
    return [len(entities["symbols"]) for entities in all_entities]


def f_tweet_polls_in_entities_counts(timeline: UserTimeline) -> List[int]:
    all_entities = timeline.get_tweet_attr("entities", {})
    return [len(entities["polls"]) for entities in all_entities]


FUNCS = {
    "tweet_types": f_tweet_types,
    "tweet_sources": f_tweet_sources,
    "tweet_places": f_tweet_places,
    "tweet_filter_levels": f_tweet_filter_levels,
    "tweet_langs": f_tweet_langs,
    "all_tweet_time_differences": f_all_tweet_time_differences,
    "ordinary_tweet_time_differences": f_ordinary_tweet_time_differences,
    "retweet_tweet_time_differences": f_retweet_tweet_time_differences,
    "quote_tweet_time_differences": f_quote_tweet_time_differences,
    "mention_tweet_time_differences": f_mention_tweet_time_differences,
    "all_tweet_texts": f_all_tweet_texts,
    "ordinary_tweet_texts": f_ordinary_tweet_texts,
    "retweet_tweet_texts": f_retweet_tweet_texts,
    "quote_tweet_texts": f_quote_tweet_texts,
    "mention_tweet_texts": f_mention_tweet_texts,
    "tweet_has_coordinates": f_tweet_has_coordinates,
    "tweet_is_possibly_sensitive": f_tweet_is_possibly_sensitive,
    "tweet_is_withheld_copyright": f_tweet_is_withheld_copyright,
    "tweet_withheld_in_countries_count": f_tweet_withheld_in_countries_count,
    "tweet_quote_counts": f_tweet_quote_counts,
    "tweet_reply_counts": f_tweet_reply_counts,
    "tweet_retweet_counts": f_tweet_retweet_counts,
    "tweet_favorite_counts": f_tweet_favorite_counts,
    "tweet_hashtags_in_entities_counts": f_tweet_hashtags_in_entities_counts,
    "tweet_urls_in_entities_counts": f_tweet_urls_in_entities_counts,
    "tweet_user_mentions_in_entities_counts": f_tweet_user_mentions_in_entities_counts,
    "tweet_media_in_entities_counts": f_tweet_media_in_entities_counts,
    "tweet_symbols_in_entities_counts": f_tweet_symbols_in_entities_counts,
    "tweet_polls_in_entities_counts": f_tweet_polls_in_entities_counts,
}
