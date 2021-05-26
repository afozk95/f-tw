from typing import Any, Dict
import regex
from .string_features import (
    n_urls,
    n_uq_urls,
    n_hashtags,
    n_uq_hashtags,
    n_mentions,
    n_uq_mentions,
)
from .utils import (
    text_cleaner,
)


# TextFeatures

def n_charS(text: str) -> int:
    text = regex.sub("\\s", "", text)
    return len(text)


def tweet_features(text: str) -> Dict[str, Any]:
    output = {}

    output["n_urls"] = n_urls(text, method="text")
    output["n_uq_urls"] = n_uq_urls(text, method="text")
    output["n_hashtags"] = n_hashtags(text, method="text")
    output["n_uq_hashtags"] = n_uq_hashtags(text, method="text")
    output["n_mentions"] = n_mentions(text, method="text")
    output["n_uq_mentions"] = n_uq_mentions(text, method="text")

    text = text_cleaner(text)
