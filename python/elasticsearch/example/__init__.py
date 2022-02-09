from elasticsearch import Elasticsearch

ELASTIC_URL = "http://localhost:9200"

CLIENT = Elasticsearch(ELASTIC_URL)