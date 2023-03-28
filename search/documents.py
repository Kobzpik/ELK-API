from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from search.models import Search


@registry.register_document
class SearchDocument(Document):
    
    TimeStamp = fields.TextField(
        attr='TimeStamp',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    From = fields.TextField(
        attr='From',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    To = fields.TextField(
        attr='To',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    Body = fields.TextField(
        attr='Body',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    Status = fields.TextField(
        attr='Status',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    SentDate = fields.TextField(
        attr='SentDate',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    ApiVersion = fields.TextField(
        attr='ApiVersion',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    NumSegments = fields.TextField(
        attr='NumSegments',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    AccountSid = fields.TextField(
        attr='AccountSid',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    Sid = fields.TextField(
        attr='Sid',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    AccountSid = fields.TextField(
        attr='AccountSid',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    Direction = fields.TextField(
        attr='Direction',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    Price = fields.TextField(
        attr='Price',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    PriceUnit = fields.TextField(
        attr='PriceUnit',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )

    class Index:
        name = 'logs_index'
     
    class Django:
        model = Search

   
