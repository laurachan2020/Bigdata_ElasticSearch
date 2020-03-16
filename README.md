# STA9760 Project 2 Insert Data into ElasticSearch


## How to Run

Start:

```
docker-compose up -d
```

This will start ElasticSearch and Kibana.

**ElasticSearch**: http://localhost:9200
**Kibana**: http://localhost:5601

Both should load...something but will be empty as python has not yet run. If nothing shows up, give it a minute as it takes a bit of time for these services to load.

Running python:

```
docker-compose run pyth python tickets.py --page_size=10 --num_pages=2


```

This will violation parking data into Elasticsearch 

sh test_curl.sh > output.txt

Shutting off:

```
docker-compose down
```
