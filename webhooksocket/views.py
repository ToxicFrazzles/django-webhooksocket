from django.shortcuts import render
from django.http import HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Bridge


def hooks(request, ident):
    try:
        bridge = Bridge.objects.get(hook_ident=ident)
    except Bridge.DoesNotExist:
        return HttpResponse(b"Thanks but no thanks!")
    print(bridge.name)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(f"Bridge{bridge.id}", {
        "type": "hook.event",
        "message": "A webhook event has ocurred"
    })
    return HttpResponse(b"Thanks!")


def dummy(request):
    return render(request, "webhooksocket/index.html")
