from typing import Any, Dict, List, Optional, Union
import datetime as dt
from dateutil import parser


class UserTimeline:
    def __init__(
        self,
        user_timeline: List[Dict[str, Any]],
        probe_time: Optional[Union[str, dt.datetime]] = None,
        datetime_format: Optional[str] = None,
    ) -> None:
        self.user_timeline = user_timeline
        self.probe_time = self._make_probe_time_attr(probe_time, datetime_format)

    def _parse_time_str(self, time_str: str, datetime_format: Optional[str] = None) -> dt.datetime:
        TWITTER_API_DATETIME_FORMAT = "%a %b %d %H:%M:%S %z %Y"
        if datetime_format is None:
            try:
                return dt.datetime.strptime(time_str, TWITTER_API_DATETIME_FORMAT)
            except Exception as _:
                return parser.parse(time_str)
        else:
            return dt.datetime.strptime(time_str, datetime_format)

    def _make_probe_time_attr(self, probe_time: Optional[Union[str, dt.datetime]], datetime_format: Optional[str] = None) -> dt.datetime:
        if isinstance(probe_time, dt.datetime):
            return probe_time
        elif isinstance(probe_time, str):
            try:
                return self._parse_time_str(probe_time, datetime_format)
            except Exception:
                raise ValueError(f"Error in probe_time, cannot convert: {probe_time}")
        elif probe_time is None:
            # print("The value for probe_time is passed as None. Assuming it as 'now'. This might not be what you want.")
            return dt.datetime.now(dt.timezone.utc)
        else:
            raise ValueError("Unknown type for probe_time")

    def _get_tweet_attr_helper(self, tweet: Dict[str, Any], field_name: str, default_value: Any = None) -> Any:
        value = tweet.get(field_name, None)
        return value if value is not None else default_value

    def get_tweet_attr(self, field_name: str, default_value: Any = None, tweets: Optional[List[Dict[str, Any]]] = None) -> List[Any]:
        if tweets is None:
            tweets = self.user_timeline

        return [self._get_tweet_attr_helper(tweet, field_name, default_value) for tweet in tweets]

    def get_tweet_attrs(self, attrs: List[Dict[str, Any]], tweets: Optional[List[Dict[str, Any]]] = None) -> List[Dict[str, Any]]:
        if tweets is None:
            tweets = self.user_timeline

        return [
            {
                attr["field_name"]: self._get_tweet_attr_helper(tweet, attr["field_name"], attr["default_value"])
                for attr in attrs
            }
            for tweet in tweets
        ]

    def _is_ordinary_tweet(self, tweet_obj: Dict[str, Any]) -> bool:
        c1 = self._is_retweet_tweet(tweet_obj)
        c2 = self._is_quote_tweet(tweet_obj)
        c3 = self._is_mention_tweet(tweet_obj)
        return not (c1 or c2 or c3)

    def _is_retweet_tweet(self, tweet_obj: Dict[str, Any]) -> bool:
        return tweet_obj.get("retweeted_status", None) is not None

    def _is_quote_tweet(self, tweet_obj: Dict[str, Any]) -> bool:
        return tweet_obj.get("quoted_status", None) is not None

    def _is_mention_tweet(self, tweet_obj: Dict[str, Any]) -> bool:
        return tweet_obj.get("in_reply_to_status_id_str", None) is not None

    def get_tweet_type(self, tweet_obj: Dict[str, Any]) -> str:
        if self._is_retweet_tweet(tweet_obj):
            return "retweet"
        elif self._is_quote_tweet(tweet_obj):
            return "quote"
        elif self._is_mention_tweet(tweet_obj):
            return "mention"
        else:
            return "ordinary"

    def get_all_tweets(self) -> List[Dict[str, Any]]:
        return self.user_timeline

    def get_ordinary_tweets(self) -> List[Dict[str, Any]]:
        return [
            tweet
            for tweet in self.user_timeline
            if self._is_ordinary_tweet(tweet)
        ]

    def get_retweet_tweets(self) -> List[Dict[str, Any]]:
        return [
            tweet
            for tweet in self.user_timeline
            if self._is_retweet_tweet(tweet)
        ]

    def get_quote_tweets(self) -> List[Dict[str, Any]]:
        return [
            tweet
            for tweet in self.user_timeline
            if self._is_quote_tweet(tweet)
        ]

    def get_mention_tweets(self) -> List[Dict[str, Any]]:
        return [
            tweet
            for tweet in self.user_timeline
            if self._is_mention_tweet(tweet)
        ]


def get_tweet_time_differences_in_sec(tweet_created_ats: List[Union[str, dt.datetime]]) -> List[float]:
    tweet_created_ats = [dt.datetime.strptime(el) if isinstance(el, str) else el for el in tweet_created_ats]
    tweet_created_ats = sorted(tweet_created_ats, reverse=False)
    return [(tw2 - tw1).total_seconds() for tw1, tw2 in zip(tweet_created_ats[:-1], tweet_created_ats[1:])]
