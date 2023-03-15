from django.shortcuts import render
import abc

from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from elasticsearch import Elasticsearch

from rest_framework import viewsets,serializers
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

# Create your views here.
#connect elasticsearch and django
es = Elasticsearch(['http://localhost:9200'])


class ElasticsearchView(APIView):
    
    def get(self, request):
    # Define a simple Elasticsearch search query
        query = {"query": {"match_all": {}}}
        
        # Perform the search query against Elasticsearch
        try:
            response = es.search(index="logstash", body=query)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=400)

        return Response({"status": "success", "data": response})
   