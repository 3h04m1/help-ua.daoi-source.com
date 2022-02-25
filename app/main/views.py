from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def mapview(request):
    return render(request, "map.html")

# Create your views here.
