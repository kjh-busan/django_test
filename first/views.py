from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime


# Create your views here.
def index(request):
    now = datetime.now()
    context = {
        'current_date': now
    }

    return render(request, 'first/index.html', context)

def select(request):
    context = {}
    return render(request, 'first/select.html', context)

def result(request):
    chosen = request.GET['number']
    context = {
        'numbers': [chosen, 2 , 3 , 4 , 5 , 6]
    }
    return render(request, 'first/result.html', context)