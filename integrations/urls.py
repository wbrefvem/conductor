from django.conf.urls import url
from integrations import views


urlpatterns = [
    url(r'^notify-at-task/$', views.AtTaskNotificationView.as_view(), {}, name='at-notify-view')
]
