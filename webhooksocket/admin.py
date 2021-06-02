from django.contrib import admin
from .models import Bridge


class BridgeAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'hook_url', 'socket_url')
    readonly_fields = ('hook_url', 'socket_url')


admin.site.register(Bridge, BridgeAdmin)
