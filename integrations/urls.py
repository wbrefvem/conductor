from django.conf.urls import url
from integrations import views


urlpatterns = [
    url(r'^update-attask/$', views.AtTaskNotificationView.as_view(), {}, name='at-update-view')
]
