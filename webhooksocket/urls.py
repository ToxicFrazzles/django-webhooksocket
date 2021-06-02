from django.urls import path, register_converter
from . import views

app_name = "webhooksocket"


class IdentConverter:
    regex = r'[a-zA-Z0-9]{64}'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value


register_converter(IdentConverter, 'ident')

urlpatterns = [
    path('hooks/<ident:ident>', views.hooks, name='hooks'),
    path('sockets/<ident:ident>', views.dummy, name='sockets')
]
