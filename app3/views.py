from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def third_project(request):
    return HttpResponse('<h1>hi..........</h1>')
def fourth_project(request):
    return HttpResponse('<marquee>helloooo...</marquee>')
