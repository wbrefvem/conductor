from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('integrations.urls')),
    url(r'^', include('api.urls')),
    url(r'^', include('django.contrib.auth.urls'))
]
