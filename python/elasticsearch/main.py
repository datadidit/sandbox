from elasticsearch import Elasticsearch

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


def _index_data(client: Elasticsearch):
    for character in DATA:
        res = client.index(index=INDEX_NAME, id=character['id'], document=character)
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
    res = client.search(index=INDEX_NAME, query=suggestion_query)
    print(res)

if __name__ == "__main__":
    main()