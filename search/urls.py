from django.urls import path,include
from .views import SearchDocumentView , SearchView , index ,test
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register(r'logs-search', SearchDocumentView ,basename='logs-search')

urlpatterns = [
    #path('test', views.test_elasticsearch,name="test_elasticsearch"),
    path('test/', SearchView.as_view()),
    #path('test1/', include(router.urls)),
    path('index/', views.index, name='index'),
    path('index_test/', views.test, name='index_test')
    
]
urlpatterns += router.urls
