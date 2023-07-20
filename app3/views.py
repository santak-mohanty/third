from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def string_response(request):
    return HttpResponse("This is my first string responce of the day")

def second_string(request):
    return HttpResponse("This my second string response of the day")

def third_string(request):
    return HttpResponse("This is my third string response of the day")
