from django.urls import path, register_converter
from . import views
from . import consumers

app_name = "webhooksocket"


class IdentConverter:
    regex = r'[a-zA-Z0-9]{64}'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value


register_converter(IdentConverter, 'ident')

websocket_urlpatterns = [
    path('whs/sockets/<ident:ident>', consumers.SocketConsumer.as_asgi(), name='sockets')
]
