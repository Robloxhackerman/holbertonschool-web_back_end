#!/usr/bin/env python3
"""
Write a Python function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """

    :param mongo_collection:
    :param topic:
    :return:
    """
    doc = mongo_collection.find({"topic": topic})
    list = [i for i in doc]
    return list
