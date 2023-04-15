#!/usr/bin/env python3
"""

"""
import uuid
from functools import wraps
from typing import Union, Optional, Callable

import redis


def count_calls(method: Callable) -> Callable:
    key = method.__qualname__

    @wraps(method)
    def call_counter(self, *args) -> bytes:
        self._redis.incr(key)
        return method(self, *args)

    return call_counter

def call_history(method: Callable) -> Callable:
    key = method.__qualname__

    @wraps(method)
    def history_dec(self, *args) -> bytes:
        self._redis.rpush(f'{key}:inputs', str(args))
        data = method(self, *args)
        self._redis.rpush(f'{key}:outputs', data)
        return data

    return history_dec

def replay(obj: Union[Callable, str]) -> None:
    cache = obj.__self__

    call_count = str(cache.get(cache.store.__qualname__), 'UTF-8')
    inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
    outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

    print(f'{obj.__qualname__} was called {call_count} times:')

    for input, output in zip(inputs, outputs):
        input, output = str(input, 'UTF-8'), str(output, 'UTF-8')
        print(f'{obj.__qualname__}(*{input}) -> {output}')


class Cache:
    """

    """
    def __init__(self):
        """

        :return:
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
