from typing import Dict, List, Optional
import regex
from .constants import (
    FIRST_PERSON,
    FIRST_PERSONP,
    SECOND_PERSON,
    SECOND_PERSONP,
    THIRD_PERSON,
    TOBE,
    PREPOSITION,
    FIRST_PERSON_PATTERN,
    FIRST_PERSONP_PATTERN,
    SECOND_PERSON_PATTERN,
    SECOND_PERSONP_PATTERN,
    THIRD_PERSON_PATTERN,
    TOBE_PATTERN,
    PREPOSITION_PATTERN,
)
from .utils import (
    get_tokens,
    get_unique_elements,
)


def get_all_pos_features(
    text: str,
    tokens: Optional[List[str]] = None,
) -> Dict[str, float]:
    tokens = get_tokens(text, tokens)

    output = {}

    output["n_first_person"] = n_first_person(text, tokens)
    output["n_uq_first_person"] = n_uq_first_person(text, tokens)
    output["n_first_personp"] = n_first_personp(text, tokens)
    output["n_uq_first_personp"] = n_uq_first_personp(text, tokens)
    output["n_second_person"] = n_second_person(text, tokens)
    output["n_uq_second_person"] = n_uq_second_person(text, tokens)
    output["n_second_personp"] = n_second_personp(text, tokens)
    output["n_uq_second_personp"] = n_uq_second_personp(text, tokens)
    output["n_third_person"] = n_third_person(text, tokens)
    output["n_uq_third_person"] = n_uq_third_person(text, tokens)
    output["n_tobe"] = n_tobe(text, tokens)
    output["n_uq_tobe"] = n_uq_tobe(text, tokens)
    output["n_prepositions"] = n_prepositions(text, tokens)
    output["n_uq_prepositions"] = n_uq_prepositions(text, tokens)

    return output


# Features

def n_first_person(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(
            FIRST_PERSON_PATTERN,
            text,
            flags=regex.IGNORECASE,
        )
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.lower() in FIRST_PERSON,
                tokens,
            )
        )
    return len(result)


def n_uq_first_person(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(
            FIRST_PERSON_PATTERN,
            text,
            flags=regex.IGNORECASE,
        )
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.lower() in FIRST_PERSON,
                tokens,
            )
        )
    return len(get_unique_elements(result))


def n_first_personp(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(
            FIRST_PERSONP_PATTERN,
            text,
            flags=regex.IGNORECASE,
        )
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.lower() in FIRST_PERSONP,
                tokens,
            )
        )
    return len(result)


def n_uq_first_personp(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(
            FIRST_PERSONP_PATTERN,
            text,
            flags=regex.IGNORECASE,
        )
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.lower() in FIRST_PERSONP,
                tokens,
            )
        )
    return len(get_unique_elements(result))


def n_second_person(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(
            SECOND_PERSON_PATTERN,
            text,
            flags=regex.IGNORECASE,
        )
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.lower() in SECOND_PERSON,
                tokens,
            )
        )
    return len(result)


def n_uq_second_person(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(
            SECOND_PERSON_PATTERN,
            text,
            flags=regex.IGNORECASE,
        )
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.lower() in SECOND_PERSON,
                tokens,
            )
        )
    return len(get_unique_elements(result))


def n_second_personp(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(
            SECOND_PERSONP_PATTERN,
            text,
            flags=regex.IGNORECASE,
        )
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.lower() in SECOND_PERSONP,
                tokens,
            )
        )
    return len(result)


def n_uq_second_personp(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(
            SECOND_PERSONP_PATTERN,
            text,
            flags=regex.IGNORECASE,
        )
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.lower() in SECOND_PERSONP,
                tokens,
            )
        )
    return len(get_unique_elements(result))


def n_third_person(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(
            THIRD_PERSON_PATTERN,
            text,
            flags=regex.IGNORECASE,
        )
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.lower() in THIRD_PERSON,
                tokens,
            )
        )
    return len(result)


def n_uq_third_person(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(
            THIRD_PERSON_PATTERN,
            text,
            flags=regex.IGNORECASE,
        )
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.lower() in THIRD_PERSON,
                tokens,
            )
        )
    return len(get_unique_elements(result))


def n_tobe(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(
            TOBE_PATTERN,
            text,
            flags=regex.IGNORECASE,
        )
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.lower() in TOBE,
                tokens,
            )
        )
    return len(result)


def n_uq_tobe(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(
            TOBE_PATTERN,
            text,
            flags=regex.IGNORECASE,
        )
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.lower() in TOBE,
                tokens,
            )
        )
    return len(get_unique_elements(result))


def n_prepositions(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(
            PREPOSITION_PATTERN,
            text,
            flags=regex.IGNORECASE,
        )
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.lower() in PREPOSITION,
                tokens,
            )
        )
    return len(result)


def n_uq_prepositions(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(
            PREPOSITION_PATTERN,
            text,
            flags=regex.IGNORECASE,
        )
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.lower() in PREPOSITION,
                tokens,
            )
        )
    return len(get_unique_elements(result))
