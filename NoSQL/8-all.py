#!/usr/bin/env python3
""" Function that lists all documents in a collection """


def list_all(mongo_collection):
    """Lists all documents in the specified MongoDB collection.

    Args:
        mongo_collection
        List of documents
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
