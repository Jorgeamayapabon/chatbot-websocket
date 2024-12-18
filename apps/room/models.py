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