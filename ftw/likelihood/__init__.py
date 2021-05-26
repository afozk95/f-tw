from typing import Any, Dict, Tuple, Union
from pathlib import Path
from .ngram import (
    infer_ngram_order_values,
    get_loglikelihoods,
)
from .utils import read_pickle


def get_model_path(col_name: str, order: Union[int, Tuple[int, int]] = 2) -> Path:
    ngram_order_values = infer_ngram_order_values(order)
    order_min, order_max = min(ngram_order_values), max(ngram_order_values)
    path = Path(__file__).parent / "models" / "ngram" / col_name / f"{order_min}_{order_max}" / "model.pkl"
    return path


def get_all_ngram_loglikelihood_features(text: str, col_name: str, order: Union[int, Tuple[int, int]] = 2) -> Dict[str, Any]:
    model_path = get_model_path(col_name, order)
    model = read_pickle(model_path)

    return get_loglikelihoods(text, model)
