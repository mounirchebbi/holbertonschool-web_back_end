#!/usr/bin/env python3
""" Function that updates topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """Update 'topics' field with the given name

    Args:
        mongo_collection
        name (str)
        topics (list)
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
