from django.shortcuts import render

# Create your views here.
def route_view(request):
    return render(request, "metro/route.html")

def map_view(request):
    return render(request, "metro/map.html")