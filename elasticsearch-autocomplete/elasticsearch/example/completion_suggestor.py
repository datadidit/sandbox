'''
    Following the docs from Elastic Search for creating a suggestor
    https://www.elastic.co/guide/en/elasticsearch/reference/current/search-suggesters.html#completion-suggester
'''
from example import CLIENT
import json

INDEX_NAME = "completion-suggestor"


def create_index():
    suggestor_mapping = {
        "mappings": {
            "properties": {
                "suggest": {
                    "type": "completion"
                },
                "title": {
                    "type": "keyword"
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
    # Index the suggestions
    index_ex_1 = {
      "suggest": {
        "input": ["Nevermind", "Nirvana" ],
        "weight": 34
      }
    }

    # Index this object with this id
    res = CLIENT.index(index=INDEX_NAME, id=1, document=index_ex_1, refresh=True)
    print(res)


def search_index():
    # Search the index
    search = {
      "suggest": {
        "song-suggest": {
          "prefix": "nir",
          "completion": {
              "field": "suggest"
          }
        }
      }
    }

    res = CLIENT.search(search, INDEX_NAME)
    print(json.dumps(res, indent=4))

    # Search with just the source
    # Search and only bring back suggestions
    search_suggestions_only = {
        "_source": "suggest",
        "suggest": {
            "song-suggest": {
                "prefix": "nir",
                "completion": {
                    "field": "suggest"
                }
            }
        }
    }
    res = CLIENT.search(search_suggestions_only, INDEX_NAME)
    print(json.dumps(res, indent=4))

    # Search with fuzziness on
    search_fuzzy_enabled = {
        "suggest": {
            "song-suggest": {
                "prefix": "nor",
                "completion": {
                    "field": "suggest",
                    "fuzzy": {
                        "fuzziness": 2
                    }
                }
            }
        }
    }

    res = CLIENT.search(search_fuzzy_enabled, INDEX_NAME)
    print(json.dumps(res, indent=4))


if __name__ == "__main__":
    # Create the index
    create_index()

    # Add Data
    index_data()

    # Search the index
    search_index()
