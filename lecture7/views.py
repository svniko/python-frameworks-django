from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Django. Lecture7</h1>')

def hello(request, name=None):
    return HttpResponse(f'<h1>Hello, {name}</h1>')

def hello_(request):
    return HttpResponse(f'<h1>Hello</h1>')


def hi(request, name=None):
    return render(request, 'lecture7/index.html',
                  {'name': name}
                  )