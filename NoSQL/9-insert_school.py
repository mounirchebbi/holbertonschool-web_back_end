#!/usr/bin/env python3
""" Function that inserts a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """Insert new document into MongoDB collection

    Args:
        mongo_collection
        **kwargs
    Returns:
        _id of the new document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
