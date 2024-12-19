from django.db import models
from django.utils.translation import gettext_lazy as _


class ChatRoomModel(models.Model):
    name = models.CharField(
        verbose_name=_("Chat Room Name"),
        max_length=100, 
        unique=True
    )

    def __str__(self):
        return self.room_name

    class Meta:
        verbose_name = _("Chat Room")
        verbose_name_plural = _("Chat Rooms")
        db_table = "apps_chat_room"


class ConnectedUserModel(models.Model):
    username = models.CharField(
        verbose_name=_("Username"),
        max_length=100
    )
    room = models.ForeignKey(
        ChatRoomModel,
        verbose_name=_("Chat Room"),
        on_delete=models.CASCADE,
        related_name="connected_users",
    )
    connected_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _("Connected User")
        verbose_name_plural = _("Connected Users")
        db_table = "apps_connected_user"
