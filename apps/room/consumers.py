import json

from django.utils import dateformat, timezone
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import redis

REDIS_PREFIX = "chat_room_users"


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("------------------Connected------------------")
        self.id = self.scope['url_route']['kwargs']['room_id']
        self.username = self.scope['url_route']['kwargs']['username']
        self.room_group_name = f'chat_{self.id}'
        
        self.user = self.scope['user']

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        
        await self.accept()
        
        # Guardar usuario en Redis
        await self.add_user_to_room(self.username, self.id)

        # Notificar a todos en la sala
        await self.update_users_in_room()
    
    async def disconnect(self, close_code):
        print("------------------Disconnected------------------")
        # Remueve usuario de Redis
        await self.remove_user_from_room(self.username, self.id)

        # Notificar a todos en la sala
        await self.update_users_in_room()
        
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)
   
    async def receive(self, text_data):
        print(f"------------------Received: {text_data}------------------")

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.username,
                'datetime': dateformat.format(timezone.now(), 'Y-m-d H:i:s')
            }
        )

        print(message)

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        datetime = event['datetime']
        await self.send(text_data=json.dumps({ 'message':message, 'username':username, 'datetime':datetime }))

    async def update_users_in_room(self):
        users = await self.get_users_in_room(self.id)

        # Notificar usuarios conectados
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_list',
                'users': users
            }
        )

    async def user_list(self, event):
        users = event['users']

        # Enviar lista de usuarios al cliente
        await self.send(text_data=json.dumps({
            'type': 'user_list',
            'users': users,
        }))

    @database_sync_to_async
    def add_user_to_room(self, username, room_id):
        r = redis.Redis(host='localhost', port=6379, db=0)
        redis_key = f"{REDIS_PREFIX}:{room_id}"
        r.sadd(redis_key, username)

    @database_sync_to_async
    def remove_user_from_room(self, username, room_id):
        r = redis.Redis(host='localhost', port=6379, db=0)
        redis_key = f"{REDIS_PREFIX}:{room_id}"
        r.srem(redis_key, username)

    @database_sync_to_async
    def get_users_in_room(self, room_id):
        r = redis.Redis(host='localhost', port=6379, db=0)
        redis_key = f"{REDIS_PREFIX}:{room_id}"
        users = r.smembers(redis_key)
        return [user.decode("utf-8") for user in users]
