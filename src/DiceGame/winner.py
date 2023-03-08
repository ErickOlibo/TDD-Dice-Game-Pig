"""This module manages the characteristics of the winner object."""
import time


class Winner:
    """Serve as a data structure to save game's winner stats."""

    def __init__(self, name: str, score: int, stamp=round(time.time())):
        self._stamp = stamp
        self._name = name
        self._score = score
        self._data = [self._stamp, self._name, self._score]

    @property
    def data(self) -> list:
        return self._data

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def to_string(self) -> str:
        return f'{self._stamp} | {self._name} - {self._score}'

    def get_name(self) -> str:
        return self._name
