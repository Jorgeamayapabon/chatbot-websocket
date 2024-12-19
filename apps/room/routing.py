from django.urls import path
from apps.room.consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/room/<username>/<room_id>', ChatConsumer.as_asgi()),
]
