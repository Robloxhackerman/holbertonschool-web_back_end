#!/usr/bin/env python3
"""

"""
import uuid
from typing import Union

import redis


class Cache:
    """

    """
    def __int__(self):
        """

        :return:
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int or float]) -> str:
        """

        :param data:
        :return:
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key