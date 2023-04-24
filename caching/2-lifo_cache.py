#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from
BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    aaaaaaaaa
    """
    def __init__(self):
        """
        aaaaaaa
        """
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
                adios = self.keys.pop(len(self.keys) - 1)
                del self.cache_data[adios]
                print(f'DISCARD: {adios}')

    def get(self, key):
        """

        :param key:
        :return:
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
