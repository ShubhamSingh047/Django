# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def montly_challenge(req, month):
    challenge = None
    if month == 'january':
        challenge = "this is January !"
    elif month == "feburary":
        challenge = "this is Feburary !"
    else:
        return HttpResponseNotFound("This Month is not supported Yet !")
    return HttpResponse(challenge)
