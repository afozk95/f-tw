from typing import Any, Dict, List, Optional
import emoji
import regex
import string
from .constants import (
    DIGIT_PATTERN,
    NUMBER_PATTERN,
    HASHTAG_PATTERN,
    MENTION_PATTERN,
    COMMA_PATTERN,
    PERIOD_PATTERN,
    EXCLAIM_PATTERN,
    EXTRASPACE_PATTERN,
    UPPER_PATTERN,
    LOWER_PATTERN,
    EMOJI_PATTERN,
    URL_PATTERN,
    NONASCII_PATTERN,
    PUNCTUATION_PATTERN,
)
from .utils import (
    get_tokens,
    get_unique_elements,
)


def get_all_string_features(
    text: str,
    tokens: Optional[List[str]] = None,
) -> Dict[str, float]:
    tokens = get_tokens(text, tokens)

    output = {}

    output["n_words"] = n_words(text, tokens)
    output["n_uq_words"] = n_uq_words(text, tokens)
    output["n_chars"] = n_chars(text, tokens)
    output["n_uq_chars"] = n_uq_chars(text, tokens)
    output["n_digits"] = n_digits(text, tokens)
    output["n_uq_digits"] = n_uq_digits(text, tokens)
    output["n_numbers"] = n_numbers(text, tokens)
    output["n_uq_numbers"] = n_uq_numbers(text, tokens)
    output["n_hashtags"] = n_hashtags(text, tokens)
    output["n_uq_hashtags"] = n_uq_hashtags(text, tokens)
    output["n_mentions"] = n_mentions(text, tokens)
    output["n_uq_mentions"] = n_uq_mentions(text, tokens)
    output["n_commas"] = n_commas(text, tokens)
    output["n_periods"] = n_periods(text, tokens)
    output["n_exclaims"] = n_exclaims(text, tokens)
    output["n_extraspaces"] = n_extraspaces(text, tokens)
    output["n_uppers"] = n_uppers(text, tokens)
    output["n_uq_uppers"] = n_uq_uppers(text, tokens)
    output["n_lowers"] = n_lowers(text, tokens)
    output["n_uq_lowers"] = n_uq_lowers(text, tokens)
    output["n_emojis"] = n_emojis(text, tokens)
    output["n_uq_emojis"] = n_uq_emojis(text, tokens)
    output["n_urls"] = n_urls(text, tokens)
    output["n_uq_urls"] = n_uq_urls(text, tokens)
    output["n_nonasciis"] = n_nonasciis(text, tokens)
    output["n_uq_nonasciis"] = n_uq_nonasciis(text, tokens)
    output["n_punctuations"] = n_punctuations(text, tokens)
    output["n_uq_punctuations"] = n_uq_punctuations(text, tokens)
    output["ratio_lowers_chars"] = ratio_lowers_chars(text, tokens, **output)
    output["ratio_uppers_chars"] = ratio_uppers_chars(text, tokens, **output)
    output["ratio_digits_chars"] = ratio_digits_chars(text, tokens, **output)
    output["ratio_chars_words"] = ratio_chars_words(text, tokens, **output)

    return output


# Features

def n_words(
    text: str,
    tokens: Optional[List[str]] = None,
) -> int:
    tokens = get_tokens(text, tokens)
    return len(tokens)


def n_uq_words(
    text: str,
    tokens: Optional[List[str]] = None,
) -> int:
    tokens = get_tokens(text, tokens)
    return len(get_unique_elements(tokens))


def n_chars(
    text: str,
    tokens: Optional[List[str]] = None,
) -> int:
    return len(text)


def n_uq_chars(
    text: str,
    tokens: Optional[List[str]] = None,
) -> int:
    return len(get_unique_elements(text))


def n_digits(
    text: str,
    tokens: Optional[List[str]] = None,
) -> int:
    result = regex.findall(DIGIT_PATTERN, text)
    return len(result)


def n_uq_digits(
    text: str,
    tokens: Optional[List[str]] = None,
) -> int:
    result = regex.findall(DIGIT_PATTERN, text)
    return len(get_unique_elements(result))


def n_numbers(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(NUMBER_PATTERN, text)
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: str.isnumeric(x),
                tokens,
            )
        )
    return len(result)


def n_uq_numbers(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(NUMBER_PATTERN, text)
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: str.isnumeric(x),
                tokens,
            )
        )
    return len(get_unique_elements(result))


def n_hashtags(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(HASHTAG_PATTERN, text)
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.startswith("#") and len(x) > 1,
                tokens,
            )
        )
    return len(result)


def n_uq_hashtags(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(HASHTAG_PATTERN, text)
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.startswith("#") and len(x) > 1,
                tokens,
            )
        )
    return len(get_unique_elements(result))


def n_mentions(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(MENTION_PATTERN, text)
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.startswith("@") and len(x) > 1,
                tokens,
            )
        )
    return len(result)


def n_uq_mentions(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(MENTION_PATTERN, text)
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.startswith("@") and len(x) > 1,
                tokens,
            )
        )
    return len(get_unique_elements(result))


def n_commas(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(COMMA_PATTERN, text)
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x == ",",
                tokens,
            )
        )
    return len(result)


def n_periods(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(PERIOD_PATTERN, text)
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x == ".",
                tokens,
            )
        )
    return len(result)


def n_exclaims(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(EXCLAIM_PATTERN, text)
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x == "!",
                tokens,
            )
        )
    return len(result)


def n_extraspaces(
    text: str,
    tokens: Optional[List[str]] = None,
) -> int:
    result = regex.findall(EXTRASPACE_PATTERN, text)
    return len(result)


def n_uppers(
    text: str,
    tokens: Optional[List[str]] = None,
) -> int:
    result = regex.findall(UPPER_PATTERN, text)
    return len(result)


def n_uq_uppers(
    text: str,
    tokens: Optional[List[str]] = None,
) -> int:
    result = regex.findall(UPPER_PATTERN, text)
    return len(get_unique_elements(result))


def n_lowers(
    text: str,
    tokens: Optional[List[str]] = None,
) -> int:
    result = regex.findall(LOWER_PATTERN, text)
    return len(result)


def n_uq_lowers(
    text: str,
    tokens: Optional[List[str]] = None,
) -> int:
    result = regex.findall(LOWER_PATTERN, text)
    return len(get_unique_elements(result))


def n_emojis(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(EMOJI_PATTERN, text)
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x in emoji.UNICODE_EMOJI,
                tokens,
            )
        )
    return len(result)


def n_uq_emojis(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(EMOJI_PATTERN, text)
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x in emoji.UNICODE_EMOJI,
                tokens,
            )
        )
    return len(get_unique_elements(result))


def n_urls(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(URL_PATTERN, text)
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.startswith("https"),
                tokens,
            )
        )
    return len(result)


def n_uq_urls(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(URL_PATTERN, text)
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x.startswith("https"),
                tokens,
            )
        )
    return len(get_unique_elements(result))


def n_nonasciis(
    text: str,
    tokens: Optional[List[str]] = None,
) -> int:
    parsed_text = text.encode(encoding="ASCII", errors="namereplace").decode()
    result = regex.findall(NONASCII_PATTERN, parsed_text)
    return len(result)


def n_uq_nonasciis(
    text: str,
    tokens: Optional[List[str]] = None,
) -> int:
    parsed_text = text.encode(encoding="ASCII", errors="namereplace").decode()
    result = regex.findall(NONASCII_PATTERN, parsed_text)
    return len(get_unique_elements(result))


def n_punctuations(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(PUNCTUATION_PATTERN, text)
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x in string.punctuation,
                tokens,
            )
        )
    return len(result)


def n_uq_punctuations(
    text: str,
    tokens: Optional[List[str]] = None,
    method: str = "tokens",  # "tokens" or "text"
) -> int:
    if method == "text":
        result = regex.findall(PUNCTUATION_PATTERN, text)
    elif method == "tokens":
        tokens = get_tokens(text, tokens)
        result = list(
            filter(
                lambda x: x in string.punctuation,
                tokens,
            )
        )
    return len(get_unique_elements(result))


# Extended Features

def ratio_lowers_chars(
    text: str,
    tokens: Optional[List[str]] = None,
    **kwargs: Any,
) -> Optional[float]:
    if all(key in kwargs for key in ["n_lowers", "n_chars"]):
        n_lowers_val = kwargs["n_lowers"]
        n_chars_val = kwargs["n_chars"]
    else:
        n_lowers_val = n_lowers(text, tokens)
        n_chars_val = n_chars(text, tokens)

    if n_chars_val == 0:
        result = None
    else:
        result = n_lowers_val / n_chars_val

    return result


def ratio_uppers_chars(
    text: str,
    tokens: Optional[List[str]] = None,
    **kwargs: Any,
) -> Optional[float]:
    if all(key in kwargs for key in ["n_uppers", "n_chars"]):
        n_uppers_val = kwargs["n_uppers"]
        n_chars_val = kwargs["n_chars"]
    else:
        n_uppers_val = n_uppers(text, tokens)
        n_chars_val = n_chars(text, tokens)

    if n_chars_val == 0:
        result = None
    else:
        result = n_uppers_val / n_chars_val

    return result


def ratio_digits_chars(
    text: str,
    tokens: Optional[List[str]] = None,
    **kwargs: Any,
) -> Optional[float]:
    if all(key in kwargs for key in ["n_digits", "n_chars"]):
        n_digits_val = kwargs["n_digits"]
        n_chars_val = kwargs["n_chars"]
    else:
        n_digits_val = n_digits(text, tokens)
        n_chars_val = n_chars(text, tokens)

    if n_chars_val == 0:
        result = None
    else:
        result = n_digits_val / n_chars_val

    return result


def ratio_chars_words(
    text: str,
    tokens: Optional[List[str]] = None,
    **kwargs: Any,
) -> Optional[float]:
    if all(key in kwargs for key in ["n_chars", "n_words"]):
        n_chars_val = kwargs["n_chars"]
        n_words_val = kwargs["n_words"]
    else:
        n_chars_val = n_chars(text, tokens)
        n_words_val = n_words(text, tokens)

    if n_words_val == 0:
        result = None
    else:
        result = n_chars_val / n_words_val

    return result
