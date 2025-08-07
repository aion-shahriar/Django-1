from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("Hello, this is the home page of first_app!")
    return render(request, 'first_app/home.html')
