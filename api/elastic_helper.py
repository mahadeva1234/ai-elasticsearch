from elasticsearch import Elasticsearch
import re
from django.conf import settings

CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

# Password for the 'elastic' user generated by Elasticsearch
ELASTIC_PASSWORD = settings.E_PASSWORD

# Found in the 'Manage Deployment' page
CLOUD_ID = settings.E_CLOUD_ID

# Create the client instance
client = Elasticsearch(
    cloud_id=CLOUD_ID,
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

# Successful response!
# print(client.info())

def e_search(keyword):
    query_body = {"query": {"multi_match": {"query": keyword}}}


    result = client.search(index="*", body=query_body)
    # print(result)
    hits = result['hits']['hits']
    # print(hits)
    data = []
    post = {}
    for hit in hits:
        # print(hit)
        post['score'] = hit['_score']
        post['post_title'] = hit['_source']['post_title']
        post['post_url'] = hit['_source']['permalink']
        post['post_content'] = cleanhtml(hit['_source']['post_content_filtered']).strip("\n")
        data.append(post.copy())
       
    return data

# print(e_search("hello"))
