from django.shortcuts import render
import abc

from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from elasticsearch import Elasticsearch



# Create your views here.

es = Elasticsearch(['http://localhost:9200'])

def test_elasticsearch(request):
    
     # Define a simple Elasticsearch search query
        query = {"query": {"match_all": {}}}

        # Perform the search query against Elasticsearch
        try:
            response = es.search(index="logstash", body=query)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

        print(response)
        # Return a JSON response with the search results
        return JsonResponse({"status": "success", "data": response})
    