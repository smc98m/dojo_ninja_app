from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("HOMEPAGE!")

# Create your views here.
