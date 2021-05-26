from typing import Any, Dict, List, Optional, Tuple
import numpy as np
import scipy


def get_distributon_features(values: List[Any], value_type: Optional[str] = None) -> Dict[str, float]:
    value_type = infer_value_type(values, value_type)

    if value_type == "numerical":
        return get_numerical_distribution_features(values)
    elif value_type == "categorical":
        return get_categorical_distribution_features(values)
    elif value_type == "boolean":
        return get_boolean_distribution_features(values)
    else:
        raise ValueError("Value type cannot be inferred")


def infer_value_type(values: List[Any], value_type: Optional[str] = None) -> str:
    if value_type is None:
        if all(isinstance(value, (int, float, type(None))) for value in values):
            return "numerical"
        elif all(isinstance(value, (str, type(None))) for value in values):
            return "categorical"
        elif all(isinstance(value, (bool, type(None))) for value in values):
            return "boolean"
        else:
            raise ValueError("Value type cannot be inferred")
    else:
        if value_type in ["numerical", "categorical", "boolean"]:
            return value_type
        else:
            raise ValueError("Value type cannot be inferred")


def filter_out_nones(values: List[Any]) -> Tuple[List[Any], int]:
    none_count = sum([1 for el in values if el is None])
    values = [value for value in values if value is not None]
    return values, none_count


def get_numerical_distribution_features(values: List[float]) -> Dict[str, float]:
    total_count = len(values)
    values, none_count = filter_out_nones(values)
    values = np.array(values)

    if values.size <= 0:
        res_dict = {
            "nonnull_ratio": np.nan,
            "min": np.nan,
            "max": np.nan,
            "median": np.nan,
            "mean": np.nan,
            "std": np.nan,
            "skewness": np.nan,
            "kurtosis": np.nan,
            "entropy": np.nan,
        }

    else:
        res_dict = {
            "nonnull_ratio": np.float(1 - none_count / total_count),
            "min": np.min(values),
            "max": np.max(values),
            "median": np.median(values),
            "mean": np.mean(values),
            "std": np.std(values),
            "skewness": scipy.stats.skew(values),
            "kurtosis": scipy.stats.kurtosis(values),
            "entropy": scipy.stats.entropy(values),
        }

    return res_dict


def get_categorical_distribution_features(values: List[str]) -> Dict[str, float]:
    total_count = len(values)
    values, none_count = filter_out_nones(values)
    _, values = np.unique(values, return_counts=True)
    values = np.array(values)

    if values.size <= 0:
        res_dict = {
            "nonnull_ratio": np.nan,
            "unique_count": np.nan,
            "min": np.nan,
            "max": np.nan,
            "median": np.nan,
            "mean": np.nan,
            "std": np.nan,
            "skewness": np.nan,
            "kurtosis": np.nan,
            "entropy": np.nan,
        }

    else:
        res_dict = {
            "nonnull_ratio": np.float(1 - none_count / total_count),
            "unique_count": np.float(values.size),
            "min": np.min(values),
            "max": np.max(values),
            "median": np.median(values),
            "mean": np.mean(values),
            "std": np.std(values),
            "skewness": scipy.stats.skew(values),
            "kurtosis": scipy.stats.kurtosis(values),
            "entropy": scipy.stats.entropy(values),
        }

    return res_dict


def get_boolean_distribution_features(values: List[str]) -> Dict[str, float]:
    total_count = len(values)
    values, none_count = filter_out_nones(values)

    if values.size <= 0:
        res_dict = {
            "nonnull_ratio": np.nan,
            "mean": np.nan
        }

    else:
        res_dict = {
            "nonnull_ratio": np.float(1 - none_count / total_count),
            "mean": np.mean(values),
        }

    return res_dict
