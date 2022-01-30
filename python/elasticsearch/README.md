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


