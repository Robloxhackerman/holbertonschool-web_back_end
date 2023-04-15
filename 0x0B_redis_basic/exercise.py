#!/usr/bin/env python3
"""

"""
import uuid
from typing import Union, Optional, Callable

import redis


class Cache:
    """

    """
    def __init__(self):
        """

        :return:
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """

        :param data:
        :return:
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        return str(self._redis.get(key),'utf-8')

    def get_int(self, key: str) -> int:
        return int(self._redis.get(key))
