#!/usr/bin/env python3
"""

"""
import pymongo


def list_all(mongo_collection):
    """

    :param mongo_collection:
    :return:
    """
    if not mongo_collection:
        return []
    else:
        return list(mongo_collection.find())