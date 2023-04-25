#!/usr/bin/env python3
"""

"""

BaseCaching = __import__('base_caching').BaseCaching

class MRUCache(BaseCaching):

    def __init__(self):
        super().__init__()
        self.keys =[]

    def put(self, key, item):
        """

        :param key:
        :param item:
        :return:
        """
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                adios = self.keys.pop(-2)
                del self.cache_data[adios]
                print(f'DISCARD: {adios}')

    def get(self, key):
        """

        :param key:
        :return:
        """
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data.get(key)
        return None