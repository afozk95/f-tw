from __future__ import annotations
from typing import Any, Dict, List, Optional, Union
import datetime as dt
from dateutil import parser


class UserMetadata:
    def __init__(
        self,
        user_metadata: Dict[str, Any],
        probe_time: Optional[Union[str, dt.datetime]] = None,
        datetime_format: Optional[str] = None,
    ) -> None:
        self.user_metadata = user_metadata
        self.probe_time = self._make_probe_time_attr(probe_time, datetime_format)
        self.account_age_as_time_diff = self._make_account_age_as_time_diff_attr()

    @staticmethod
    def from_user_crawl_object(user_crawl_object: Dict[str, Any], user_metadata_key: str = "user", probe_time_key: str = "created_at", datetime_format: Optional[str] = None) -> UserMetadata:
        user_metadata = user_crawl_object[user_metadata_key]
        probe_time = user_crawl_object[probe_time_key]
        return UserMetadata(user_metadata, probe_time, datetime_format)

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

    def _make_account_age_as_time_diff_attr(self) -> float:
        created_at = self.user_metadata["created_at"]
        account_age_as_time_diff = self.probe_time - self._parse_time_str(created_at)
        return account_age_as_time_diff

    def get_usermetadata_attr(self, field_name: str, default_value: Any = None) -> Any:
        value = self.user_metadata.get(field_name, None)
        return value if value is not None else default_value

    def get_usermetadata_attrs(self, attrs: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {
            attr["field_name"]: self.get_usermetadata_attr(attr["field_name"], attr["default_value"])
            for attr in attrs
        }

    def get_account_age(self, time_frame: str) -> float:
        account_age_in_sec = self.account_age_as_time_diff.total_seconds()
        if time_frame == "sec":
            return account_age_in_sec
        elif time_frame == "min":
            return account_age_in_sec / 60.0
        elif time_frame == "hour":
            return account_age_in_sec / (60.0 * 60.0)
        elif time_frame == "day":
            return account_age_in_sec / (60.0 * 60.0 * 24)
        else:
            raise ValueError(f"Unknown time_frame: {time_frame}")

    @property
    def account_age(self) -> float:
        return self.get_account_age(time_frame="hour")
