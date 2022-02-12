'''
    Going through context sugggestor example
    https://www.elastic.co/guide/en/elasticsearch/reference/current/search-suggesters.html#context-suggester
'''
from example import CLIENT
import json

INDEX_NAME = "place_example"


# TODO: Add the geopoint portion to this as well.
def create_index():
    suggestor_mapping = {
        "mappings": {
            "properties": {
                "suggest": {
                    "type": "completion",
                    "contexts": [
                        {
                            "name": "place_type",
                            "type": "category"
                        },
                        {
                            "name": "location",
                            "type": "geo",
                            "precision": 4
                        }
                    ]
                }
            }
        }
    }

    iClient = CLIENT.indices
    if not iClient.exists(INDEX_NAME):
        res = iClient.create(INDEX_NAME, body=suggestor_mapping)
        print(res)
    else:
        print(f"Index {INDEX_NAME} already exists")


def index_data():
    # Index some suggestions
    data = {
        "suggest": {
            "input": ["timmy's", "starbucks", "dunkin donuts"],
            "contexts": {
                "place_type": ["cafe", "food"]
            }
        }
    }

    res = CLIENT.index(index=INDEX_NAME, id=1, document=data, refresh=True)
    return res


def search_data():
    # Search with contexts
    search = {
        "suggest": {
            "place_suggestion": {
                "prefix": "tim",
                "completion": {
                    "field": "suggest",
                    "size": 10,
                    "contexts": {
                        "place_type": ["cafe", "restaurants"]
                    }
                }
            }
        }
    }

    res = CLIENT.search(search, INDEX_NAME)
    print(json.dumps(res, indent=4))

    # Search with non matching contexts
    search = {
        "suggest": {
            "place_suggestion": {
                "prefix": "tim",
                "completion": {
                    "field": "suggest",
                    "size": 10,
                    "contexts": {
                        "place_type": ["nomatch"]
                    }
                }
            }
        }
    }

    res = CLIENT.search(search, INDEX_NAME)
    print(json.dumps(res, indent=4))

    # Boost Specific Categories
    search = {
        "suggest": {
            "place_suggestion": {
                "prefix": "tim",
                "completion": {
                    "field": "suggest",
                    "size": 10,
                    "contexts": {
                        "place_type": [
                            {"context": "cafe"},
                            {"context": "restaurants", "boost": 2}
                        ]
                    }
                }
            }
        }
    }

    res = CLIENT.search(search, INDEX_NAME)
    print(json.dumps(res, indent=4))


if __name__ == "__main__":
    create_index()

    index_data()

    search_data()