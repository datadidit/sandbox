import json
from elasticsearch import Elasticsearch
from elasticsearch.client.indices import IndicesClient

ELASTIC_URL = "http://localhost:9200"

INDEX_NAME = "simpson-index"

DATA = [
    {
        'name': "Homer Simpson",
        'id': 1
    },
    {
        'name': "Marge Simpson",
        'id': 2
    },
    {
        'name': "Bart Simpson",
        'id': 3
    },
    {
        'name': "Lisa Simpson",
        'id': 4
    },
    {
        'name': "Maggie Simpson",
        'id': 5
    }
]


def delete_index():
    res = Elasticsearch(ELASTIC_URL)
    res.indices.delete(INDEX_NAME)


def _index_data(client: Elasticsearch, index_name=INDEX_NAME):
    for character in DATA:
        res = client.index(index=index_name, id=character['id'], document=character)
        print(res)
        # print(character)


# TODO: Move this hello world example somewhere else
def hello_world():
    # Create the client
    client = Elasticsearch(ELASTIC_URL)
    print(client.info())
    # Actually index the data
    # _index_data(client)
    # Get an entry from the index
    res = client.get(index=INDEX_NAME, id=1)
    print(res['_source'])

    # Refresh the test index to have all the latest operations
    client.indices.refresh(index=INDEX_NAME)

    # Search the index and match all
    res = client.search(index=INDEX_NAME, query={"match_all": {}})
    hits = res['hits']['total']['value']
    print(f"Got {hits}")

    for hit in res['hits']['hits']:
        print(f"Query hit on {hit['_source']}")


'''
    Example of using the completion suggestor API
    https://www.elastic.co/guide/en/elasticsearch/reference/current/search-suggesters.html#completion-suggester
'''



def main():
    # hello_world()
    # Now how do I use suggester api w/ this client
    suggestion_query = {
        "query": {
            "match": {
                "name": "H"
            }
        },
        "suggest": {
            "my-suggest-1": {
                "text": "H",
                "term": {
                    "field": "name"
                }
            }
        }
    }

    client = Elasticsearch(ELASTIC_URL)
    # iClient = IndicesClient(client)
    # Add a mapping
    suggester_mapping = {
        "mappings": {
            INDEX_NAME: {
                "name": {
                    "type": "completion"
                },
                "name": {
                    "type": "keyword"
                }
            }
        }
    }
    aIndex = client.reindex().get(INDEX_NAME)
    print(json.dumps(aIndex, indent=4))
    # print(iClient.get(INDEX_NAME))
    # iClient.put_mapping(suggester_mapping, index=INDEX_NAME, doc_type=None)
    # res = client.search(index=INDEX_NAME, query=suggestion_query)
    # print(res)


if __name__ == "__main__":
    # delete_index()
    # main()
    # res = Elasticsearch(ELASTIC_URL)
    # _index_data(res, index_name="test-index")
    completion_suggestor_tutoria()