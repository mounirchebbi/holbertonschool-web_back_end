#!/usr/bin/env python3
""" Function that returns the list of schools having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """Return list of schools with a specific topic

    Args:
        mongo_collection
        topic (str)

    Returns:
        List of documents "topics": topic
    """
    return list(mongo_collection.find({"topics": topic}))
