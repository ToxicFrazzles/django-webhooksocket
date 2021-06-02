from django.shortcuts import render


def dummy(request):
    return render(request, "webhooksocket/index.html")
