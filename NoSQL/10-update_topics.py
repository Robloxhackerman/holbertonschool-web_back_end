#!/usr/bin/env python3
"""
Write a Python function that changes all topics of a school document based on the name:
"""


def update_topics(mongo_collection, name, topics):
    """

    :param mongo_collection:
    :param name:
    :param topics:
    :return:
    """
    return mongo_collection.update_many({"name": name},{"$set": {"topics": topics}})
