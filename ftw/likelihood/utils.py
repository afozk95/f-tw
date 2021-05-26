from typing import Any
import pickle


def write_pickle(data: Any, path: str) -> None:
    with open(path, "wb") as f:
        pickle.dump(data, f)


def read_pickle(path: str) -> Any:
    with open(path, "rb") as f:
        data = pickle.load(f)

    return data
