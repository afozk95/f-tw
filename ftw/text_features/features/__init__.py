from typing import Any, Dict, List, Optional
import pandas as pd
from .string_features import get_all_string_features
from .pos_features import get_all_pos_features
from .sentiment_features import get_all_sentiment_features
from .word2vec_features import get_all_word2vec_features
from .utils import get_tokens


def get_all_text_features(
    text: str,
    pos: bool = True,
    sentiment: bool = True,
    word_dims: Optional[int] = None,
    verbose: bool = True,
) -> Dict[str, Any]:
    # tokenize
    tokens = get_tokens(text)

    # text features
    if verbose:
        print("Counting features in text...")
    output_string = get_all_string_features(text, tokens)

    # parts of speech
    if pos:
        if verbose:
            print("Parts of speech...")
        output_pos = get_all_pos_features(text, tokens)
    else:
        output_pos = {}

    # sentiment
    if sentiment:
        if verbose:
            print("Sentiment analysis...")
        output_sentiment = get_all_sentiment_features(text, tokens)
    else:
        output_sentiment = {}

    # get word dim estimates
    if word_dims is not None:
        if verbose:
            print("Word dimensions...")
        n_obs = 100  # TODO
        output_word_dims = get_all_word2vec_features(text, word_dims, n_obs)
    else:
        output_word_dims = {}

    output = {
        **output_string,
        **output_pos,
        **output_sentiment,
        **output_word_dims,
    }

    return output


def get_all_text_features_in_bulk_df(
    texts: List[Optional[str]],
    pos: bool = True,
    sentiment: bool = True,
    word_dims: Optional[int] = None,
    verbose: bool = True,
) -> pd.DataFrame:
    outputs = [
        get_all_text_features(text, pos, sentiment, word_dims, verbose)
        for text in texts
    ]

    df = pd.DataFrame(outputs)
    return df
