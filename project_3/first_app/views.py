from django.shortcuts import render
import datetime

# Create your views here.



def home(request):
    d={'author': 'Aion', 'age': 15, 'lst': ['python', 'is', 'best'], 'birthday': datetime.datetime.now(), 'val': '', 'courses':[
        {
            'id': 1,
            'name': 'Python',
            'duration': '3 months',
            'fee': 3000
        }
        ,
        {
            'id': 2,
            'name': 'Django',
            'duration': '2 months',
            'fee': 2000
        },
        {
            'id': 3,
            'name': 'JavaScript',
            'duration': '1 month',
            'fee': 1000
        }
    ]}
    return render(request, 'home.html', context=d)
