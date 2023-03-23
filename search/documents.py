from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from search.models import Search


@registry.register_document
class SearchDocument(Document):
    
    title = fields.TextField(
        attr='title',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    category = fields.ObjectField(
        attr='category',
        properties={
            'id': fields.IntegerField(),
            'title': fields.TextField(),
        }
    )

    class Index:
        name = 'logs_index'
     
    class Django:
        model = Search

   
