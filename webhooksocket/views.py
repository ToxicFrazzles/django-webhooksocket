from django.shortcuts import render
from django.http import HttpResponse
from .models import Bridge


def hooks(request, ident):
    bridge = Bridge.objects.get(hook_ident=ident)
    print(bridge.name)
    return HttpResponse(b"Thanks!")


def dummy(request):
    return render(request, "webhooksocket/index.html")
