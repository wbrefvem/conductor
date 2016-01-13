from django.conf.urls import include, url
from rest_framework import routers
from api import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'services', views.ServiceViewSet)
router.register(r'integrations', views.IntegrationViewSet)
router.register(r'workers', views.WorkerViewSet)
router.register(r'accounts', views.AccountViewSet)

urlpatterns = [
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls))
]
