# Elastic Search

This works through using the Elastic Search Suggestions api for providing search to
a dataset with python.

## [Elastic Search](https://www.elastic.co/)

* [Docker Tutorial](https://www.elastic.co/guide/en/elasticsearch/reference/7.16/docker.html)

* Get Image
    ```shell
    # No latest tag???
    docker pull elasticsearch:7.16.3
    ```
* Run Image

    ```
    docker run -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.16.3
    ```



## Notes
* Very good detailed [article](https://kadek-marek.medium.com/implementing-typeahead-with-elastic-search-685304f95cd5)
* [Removal Of Mappings](https://www.elastic.co/guide/en/elasticsearch/reference/current/removal-of-types.html)
* In order to get autocompletion(Suggesters) you need to add a suggestion [mapping](https://www.elastic.co/guide/en/elasticsearch/reference/6.8/search-suggesters-completion.html)
  * https://www.linkedin.com/pulse/building-auto-complete-api-elasticsearch-mihir-kelkar/
  * [Quick Start](https://www.elastic.co/guide/en/elasticsearch/reference/7.16/getting-started.html)
  * [Python Example](https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/examples.html?baymax=rec&rogue=rec-1&elektra=guide)
  * Keep getting this error when trying to add a suggestor:
  
  ```shell
  {
    "error": {
        "root_cause": [
            {
                "type": "resource_already_exists_exception",
                "reason": "index [simpson-index/Ysa6-SwLT_GZVu_y7xHiXw] already exists",
                "index_uuid": "Ysa6-SwLT_GZVu_y7xHiXw",
                "index": "simpson-index"
            }
        ],
        "type": "resource_already_exists_exception",
        "reason": "index [simpson-index/Ysa6-SwLT_GZVu_y7xHiXw] already exists",
        "index_uuid": "Ysa6-SwLT_GZVu_y7xHiXw",
        "index": "simpson-index"
    },
    "status": 400
  }
  ```
  
  * By default there doing dynamic indexing and it seems as if you can't update the index once it's been defined
