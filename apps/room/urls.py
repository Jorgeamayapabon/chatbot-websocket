from django.urls import include, path
from apps.room.api import urls
from apps.room.api.views import register, room


urlpatterns = [
    path("api", include(urls.urlpatterns)),
    path('register', register, name='register'),
    path('chat/<int:room_id>', room, name='room'),
]
