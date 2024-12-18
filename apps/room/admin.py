from django.contrib import admin
from apps.room.models import ChatRoomModel


@admin.register(ChatRoomModel)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
