#!/usr/bin/env python3
"""

"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                adios = self.keys.pop(0)
                del self.cache_data[adios]
                print(f'DISCARD: {adios}')
    def get(self, key):
        if key is not None and key in self.keys:
            return self.cache_data[key]
        else:
            return None
