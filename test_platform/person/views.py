from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    name = request.GET.get("name","")
    for i in range(3):
        talk = "hello," +name
    return HttpResponse(talk)


