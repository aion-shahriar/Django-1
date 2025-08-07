from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def courses(request):
    return HttpResponse("first_app/courses Page")

def about(request):
    return HttpResponse("first_app/About Page")
def home(request):
    return HttpResponse("first_app/home Page")
