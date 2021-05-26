from typing import Any, Dict, List, Optional, Union
import json
from nltk.tokenize.casual import TweetTokenizer
import pandas as pd
from pathlib import Path
import regex


def get_tokens(
    text: str,
    tokens: Optional[List[str]] = None,
) -> List[str]:
    if tokens is None:
        tokenizer = TweetTokenizer()
        tokens = tokenizer.tokenize(text)

    return tokens


def get_unique_elements(
    lst: List[Any],
) -> List[Any]:
    return list(set(lst))


def read_tsv(path: Union[str, Path]) -> pd.DataFrame:
    df = pd.read_csv(path, sep="\t", encoding="latin1")
    return df


def read_sentiment_tsv(method: str, is_dict: bool = False) -> pd.DataFrame:
    curr_path = Path(__file__)
    data_folder_path = curr_path.parents[1].resolve() / "data"
    sentiment_data_paths = {
        "afinn": data_folder_path / "afinn_dict.tsv",
        "bing": data_folder_path / "bing_dict.tsv",
        "syuzhet": data_folder_path / "syuzhet_dict.tsv",
        "vader": data_folder_path / "vader_dict.tsv",
        "politeness": data_folder_path / "politeness_dict.tsv",
    }

    df = read_tsv(sentiment_data_paths[method])

    if is_dict:
        return dict(zip(df["word"].tolist(), df["value"].tolist()))

    return df


def read_json(path: Union[str, Path]) -> Dict[str, Any]:
    with open(path) as json_file:
        data = json.load(json_file)

    return data


def read_sentiment_dict(method: str) -> pd.DataFrame:
    curr_path = Path(__file__)
    data_folder_path = curr_path.parents[1].resolve() / "data"
    sentiment_data_paths = {
        "afinn": data_folder_path / "afinn_dict.json",
        "bing": data_folder_path / "bing_dict.json",
        "syuzhet": data_folder_path / "syuzhet_dict.json",
        "vader": data_folder_path / "vader_dict.json",
        "politeness": data_folder_path / "politeness_dict.json",
    }

    return read_json(sentiment_data_paths[method])


def text_cleaner(text: str) -> str:
    # remove URLs, mentions (not hashtags, keep those)
    text = regex.sub("https?:[[:graph:]]+|@\\S+", "", text)

    # convert non-ascii into ascii exclamation marks
    text = regex.sub("\u00A1", "\u0021", text)
    text = regex.sub("\u01C3", "\u0021", text)
    text = regex.sub("\u202C", "\u0021", text)
    text = regex.sub("\u203D", "\u0021", text)
    text = regex.sub("\u2762", "\u0021", text)

    # convert non-ascii into ascii apostrophes
    text = regex.sub("\u2018", "\u0027", text)
    text = regex.sub("\uA78C", "\u0027", text)
    text = regex.sub("\u05F3", "\u0027", text)
    text = regex.sub("\u0301", "\u0027", text)
    text = regex.sub("\u02C8", "\u0027", text)
    text = regex.sub("\u2018", "\u0027", text)
    text = regex.sub("\u02Bc", "\u0027", text)
    text = regex.sub("\u02B9", "\u0027", text)
    text = regex.sub("\u05F3", "\u0027", text)
    text = regex.sub("\u2019", "\u0027", text)

    # convert non-ascii into ascii commas
    text = regex.sub("\u2795", "\u002B", text)

    # convert non-ascii into ascii hypthens
    text = regex.sub("\u2010", "\u002D", text)
    text = regex.sub("\u2011", "\u002D", text)
    text = regex.sub("\u2012", "\u002D", text)
    text = regex.sub("\u2013", "\u002D", text)
    text = regex.sub("\u2043", "\u002D", text)
    text = regex.sub("\u2212", "\u002D", text)
    text = regex.sub("\u10191", "\u002D", text)

    # convert non-ascii into ascii periods
    text = regex.sub("\u06D4", "\u002E", text)
    text = regex.sub("\u2E3C", "\u002E", text)
    text = regex.sub("\u3002", "\u002E", text)

    # convert non-ascii into ascii elipses
    text = regex.sub("\u2026", "\u002E\u002E\u002E", text)

    return text
