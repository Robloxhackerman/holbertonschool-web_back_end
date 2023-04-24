#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    aaaaaaaaaa
    """

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """

        :param key:
        :param item:
        :return:
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                adios = self.keys.pop(0)
                del self.cache_data[adios]
                print(f'DISCARD: {adios}')

    def get(self, key):
        """

        :param key:
        :return:
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
