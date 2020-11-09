from pymemcache.client import base

import json
from pymemcache import serde


class JsonSerde(object):
    def serialize(self, key, value):
        if isinstance(value, str):
            return value, 1
        return json.dumps(value), 2

    def deserialize(self, key, value, flags):
        if flags == 1:
            return value
        if flags == 2:
            return json.loads(value)
        raise Exception("Unknown serialization format")


def create_cache_client():
    client = base.Client(('localhost', 11211), serde=serde.PickleSerde(pickle_version=2))
    return client
