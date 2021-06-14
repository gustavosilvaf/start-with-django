from django.shortcuts import render, HttpResponse


# Create your views here.
def hello(request, name, age):
    return HttpResponse('{}, {}'.format(name, age))
