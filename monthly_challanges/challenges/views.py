from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def January(req):
    return HttpResponse("this is January !")


def feburary(req):
    return HttpResponse("this is Feburary !")
