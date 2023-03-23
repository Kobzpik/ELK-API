from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from search.documents import SearchDocument
from search.models import Search


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ['title', 'content']


class SearchDocumentSerializer(DocumentSerializer):
    class Meta:
        document = SearchDocument

        fields = (
            
        )
