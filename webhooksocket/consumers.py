from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json
from .models import Bridge


@database_sync_to_async
def get_bridge_by_sock_ident(sock_ident):
    return Bridge.objects.get(socket_ident=sock_ident)


class SocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.socket_ident = self.scope['url_route']['kwargs']['ident']
        try:
            self.bridge = await get_bridge_by_sock_ident(self.socket_ident)
        except Bridge.DoesNotExist:
            await self.close()
            return
        await self.channel_layer.group_add(
            f"Bridge{self.bridge.id}",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.socket_ident,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        print(text_data)

    async def hook_event(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
