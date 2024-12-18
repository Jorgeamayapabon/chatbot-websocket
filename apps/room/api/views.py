from rest_framework.viewsets import ModelViewSet
from apps.room.api.serializer import ChatRoomSerializer
from apps.room.models import ChatRoomModel
from rest_framework.permissions import IsAdminUser


class ChatRoomViewSet(ModelViewSet):
    queryset = ChatRoomModel.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [IsAdminUser]
