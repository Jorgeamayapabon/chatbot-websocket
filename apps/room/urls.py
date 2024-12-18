from django.urls import include, path
from apps.room.api import urls


urlpatterns = [
    path(
        'api',
        include(urls.urlpatterns)
    ),
]
