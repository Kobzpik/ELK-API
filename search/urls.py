from django.urls import path,include
from .import views

urlpatterns = [
    path('test', views.test_elasticsearch,name="test_elasticsearch")
]

