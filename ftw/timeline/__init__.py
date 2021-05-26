from typing import Any, Dict
from .utils import UserTimeline
from .funcs import FUNCS


def get_all_timeline_features(timeline: UserTimeline) -> Dict[str, Any]:
    return {
        key: func(timeline)
        for key, func in FUNCS.items()
    }
