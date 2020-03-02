from datetime import datetime
from elasticsearch import Elasticsearch


es = Elasticsearch()

doc = {
    'author': 'taqkarim',
    'text': 'Testing ElasticSearch',
    'timestamp': datetime(2012, 9, 16, 0, 0),  # in the far past
    "location": "41.12,-71.34"
}

# load a tweet into ES
res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
print(res['result'])

# query by id
res = es.get(index="test-index", doc_type='tweet', id=1)
print(res['_source'])

es.indices.refresh(index="test-index")

# search
res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
