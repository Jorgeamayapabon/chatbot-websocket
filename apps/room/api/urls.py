from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.room.api.views import ChatRoomViewSet


router = DefaultRouter()
router.register('chatroom', ChatRoomViewSet)

urlpatterns = [
    path('/', include(router.urls)),
]
