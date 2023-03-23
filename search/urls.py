from django.urls import path,include
from .views import SearchDocumentView , SearchView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'logs-search', SearchDocumentView ,basename='logs-search')

urlpatterns = [
    #path('test', views.test_elasticsearch,name="test_elasticsearch"),
    path('test/', SearchView.as_view()),
    #path('test1/', include(router.urls)),
]
urlpatterns += router.urls
