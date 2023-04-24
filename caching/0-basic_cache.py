#!/usr/bin/env python3
"""
Create a class BasicCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """

    """

    def put(self, key, item):
        """

        :param key:
        :param item:
        :return:
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """

        :param key:
        :return:
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
