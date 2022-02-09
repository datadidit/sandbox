import json
from example import CLIENT

INDEX_NAME = "simpson-example"

SIMPSON_DATA = [
    {
        "name": "Homer Simpson",
    },
    {
        "name": "Marge Simpson"
    },
    {
        "name": "Bart Simpson"
    },
    {
        "name": "Lisa Simpson"
    },
    {
        "name": "Maggie Simpson"
    }
]


'''
    Allowing the index to be created for me dynamically
'''
def create_index():
    '''
        Creates a dynamic index for each character
    :return:
    '''
    for i, character in enumerate(SIMPSON_DATA, start=1):
        print(f"{i} {character['name']}")
        CLIENT.index(index=INDEX_NAME, id=i, document=character)


def search():
    '''
        Search this index in various ways
    :return:
    '''
    # Search the index and match all
    res = CLIENT.search(index=INDEX_NAME, query={"match_all": {}})
    hits = res['hits']['total']['value']
    print(f"Got {hits} Hits")

    for hit in res['hits']['hits']:
        print(f"Query hit on {hit['_source']}")


def add_suggestor():
    '''
        Add a suggestor to the already existing index
    :return:
    '''
    iClient = CLIENT.indices
    suggest = {
        "properties": {
            "name_completion": {
                "type": "completion"
            }
        }
    }
    res = iClient.put_mapping(suggest, index=INDEX_NAME)
    print(res)


def add_suggestions():
    for i, character in enumerate(SIMPSON_DATA, start=1):
        print(f"{i} {character['name']}")
        character['name_completion'] = {
            "input": character['name'].split()
        }

        print(character)
        res = CLIENT.index(index=INDEX_NAME, id=i, document=character)
        print(res)


def search_suggestor():
    '''
        Examples of seaching for completion
    :return:
    '''
    search = {
        "suggest": {
            "simpson-suggest": {
                "prefix": "mar",
                "completion": {
                    "field": "name_completion"
                }
            }
        }
    }

    res = CLIENT.search(search, INDEX_NAME)
    print(json.dumps(res, indent=4))

    # Add some fuzziness so Maggie comes back too
    search['suggest']['simpson-suggest']['completion'] = {
        "field": "name_completion",
        "fuzzy": {
            "fuzziness": 2
        }
    }
    print(search)
    res = CLIENT.search(search, INDEX_NAME)
    print(json.dumps(res, indent=4))

    # TODO: Figure out scoring


if __name__ == "__main__":
    # create_index()
    #
    # search()
    #
    # add_suggestor()

    # add_suggestions()

    search_suggestor()