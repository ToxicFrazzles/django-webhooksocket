from django.shortcuts import render
from django.http import HttpResponse
from .models import Bridge


def hooks(request, ident):
    try:
        bridge = Bridge.objects.get(hook_ident=ident)
    except Bridge.DoesNotExist:
        return HttpResponse(b"Thanks but no thanks!")
    print(bridge.name)
    return HttpResponse(b"Thanks!")


def dummy(request):
    return render(request, "webhooksocket/index.html")
