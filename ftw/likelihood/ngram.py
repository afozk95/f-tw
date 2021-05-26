from typing import Dict, List, Optional, Union, Tuple
from nltk.util import ngrams
from nltk.lm import NgramCounter
import numpy as np
from .utils import write_pickle


def train_ngram_model(
    texts: List[str],
    order: Union[int, Tuple[int, int]] = 2,
    is_make_unique: bool = True,
    is_write_to_disk: bool = False,
    path: Optional[str] = None,
) -> NgramCounter:  # TODO
    ngram_order_values = infer_ngram_order_values(order)

    if is_make_unique:
        texts = list(set(texts))

    tokenized_texts = [
        [c for c in text] for text in texts
    ]

    ngram_counts = NgramCounter()
    ngram_counts.ngram_order_values = ngram_order_values

    for n in ngram_order_values:
        text_ngrams = [ngrams(tokenized_text, n) for tokenized_text in tokenized_texts]
        ngram_counts.update(text_ngrams)

    if is_write_to_disk:
        if path is None:
            if isinstance(order, int):
                path = f"ngram_model_{order}.pkl"
            elif isinstance(order, tuple) and len(order) == 2:
                path = f"ngram_model_{order[0]}.{order[1]}.pkl"
            else:
                path = f"ngram_model.pkl"
        write_pickle(ngram_counts, path)

    return ngram_counts


def infer_ngram_order_values(order: Union[int, Tuple[int, int]] = 2) -> List[int]:
    if isinstance(order, int):
        return [order]
    elif isinstance(order, tuple) and len(order) == 2:
        return list(range(order[0], order[1] + 1))
    else:
        raise ValueError("ngram order values cannot be inferred")


def get_loglikelihoods(
    text: str,
    ngram_model: NgramCounter,
) -> Dict[str, float]:
    def get_ngram_token_loglikelihood(ngram_model: NgramCounter, ngram_token, ngram_order: int) -> float:
        if ngram_order > 1:
            val = np.log(ngram_model[ngram_token[:-1]][ngram_token[-1]]) - np.log(max(1, ngram_model[ngram_token[:-1]].N()))
        elif ngram_order == 1:
            val = np.log(ngram_model[ngram_token[0]]) - np.log(max(1, ngram_model[1].N()))
        else:
            raise ValueError("ngram_order value cannot be negative")
        return val

    ngram_order_values = ngram_model.ngram_order_values
    tokenized_text = [c for c in text]
    ngram_tokens_by_order = {
        order: ngrams(tokenized_text, order)
        for order in ngram_order_values
    }

    loglikelihoods = {
        str(order): np.mean(
            [get_ngram_token_loglikelihood(ngram_model, ngram_token, order) for ngram_token in ngram_tokens]
        )
        for order, ngram_tokens in ngram_tokens_by_order.items()
    }

    return loglikelihoods
