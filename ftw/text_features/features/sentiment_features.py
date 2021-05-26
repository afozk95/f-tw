from typing import Dict, List, Optional
from functools import reduce
from .utils import (
    get_tokens,
    read_sentiment_tsv,
)


def get_all_sentiment_features(
    text: str,
    tokens: Optional[List[str]] = None,
) -> Dict[str, float]:
    tokens = get_tokens(text, tokens)

    output = {}

    output["sent_afinn"] = sentiment_afinn(text, tokens)
    output["sent_bing"] = sentiment_bing(text, tokens)
    output["sent_syuzhet"] = sentiment_syuzhet(text, tokens)
    output["sent_vader"] = sentiment_vader(text, tokens)
    output["sent_politeness"] = sentiment_politeness(text, tokens)

    return output


def get_generic_sentiment_score(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "afinn",
) -> float:
    sentiment_dict = read_sentiment_tsv(method, is_dict=True)

    if tokens is None:
        text = text.lower()
        tokens = get_tokens(text, tokens)
    else:
        tokens = [token.lower() for token in tokens]

    sentiment_score = reduce(
        lambda acc, el: acc + sentiment_dict.get(el.lower(), 0),
        tokens,
        0,
    )

    return sentiment_score


# Features

def sentiment_afinn(
    text: str,
    tokens: Optional[List[str]] = None,
) -> float:
    return get_generic_sentiment_score(text, tokens, "afinn")


def sentiment_bing(
    text: str,
    tokens: Optional[List[str]] = None,
) -> float:
    return get_generic_sentiment_score(text, tokens, "bing")


def sentiment_syuzhet(
    text: str,
    tokens: Optional[List[str]] = None,
) -> float:
    return get_generic_sentiment_score(text, tokens, "syuzhet")


def sentiment_vader(
    text: str,
    tokens: Optional[List[str]] = None,
) -> float:
    return get_generic_sentiment_score(text, tokens, "vader")


def sentiment_politeness(
    text: str,
    tokens: Optional[List[str]] = None,
) -> float:
    return get_generic_sentiment_score(text, tokens, "politeness")
