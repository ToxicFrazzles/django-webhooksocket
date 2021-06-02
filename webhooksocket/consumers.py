from channels.generic.websocket import AsyncWebsocketConsumer
import json


class SocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.socket_ident = self.scope['url_route']['kwargs']['ident']
        await self.channel_layer.group_add(
            self.socket_ident,
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
