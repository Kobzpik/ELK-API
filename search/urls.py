from django.urls import path,include
from .views import ElasticsearchView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', ElasticsearchView ,basename='MyModel')

urlpatterns = [
    #path('test', views.test_elasticsearch,name="test_elasticsearch"),
    path('test/', ElasticsearchView.as_view()),
    #path('test1/', include(router.urls)),
]

