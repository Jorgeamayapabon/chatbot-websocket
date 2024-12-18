from rest_framework import serializers
from apps.room.models import ChatRoomModel


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoomModel
        fields = '__all__'
