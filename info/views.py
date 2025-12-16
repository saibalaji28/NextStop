from django.shortcuts import render

def faq(request):
    return render(request, "info/faq.html")

def about(request):
    return render(request, "info/about.html")