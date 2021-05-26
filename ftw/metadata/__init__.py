from typing import Any, Dict
from .utils import UserMetadata
from .funcs import FUNCS


def get_all_metadata_features(metadata: UserMetadata) -> Dict[str, Any]:
    return {
        key: func(metadata)
        for key, func in FUNCS.items()
    }
