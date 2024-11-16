from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


montly_challenges_list = {
    "january": "Eat no meat for the entire month !",
    "february": "Walk for at least 20 minutes every day !",
    "march": "learn Django for at least 20 minutes daily!",
}

# Create your views here.


def index(req):
    list_item = ""
    month_list = list(montly_challenges_list.keys())
    for month in month_list:
        cpatilise_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_item += f"<li><a href=\"{
            month_path} \">{cpatilise_month}</a></li>"

    response_data = f"<ul>{list_item}</ul>"
    return HttpResponse(response_data)


def montly_challenge_num(req, month_num):
    try:
        month_data_key = list(montly_challenges_list.keys())
        month_data = month_data_key[month_num-1]
        # return HttpResponse(montly_challenges_list[month_data])
        redirect_path = reverse("month_challenge", args=[month_data])
        return HttpResponseRedirect('/challenges/'+month_data)
    except:
        return HttpResponseNotFound("No such key value present for number !")


def montly_challenge(req, month):
    # challenge = None
    # if month == 'january':
    #     challenge = "this is January !"
    # elif month == "feburary":
    #     challenge = "this is Feburary !"
    try:
        challenge = montly_challenges_list[month]
        response_data = f"<h1>{challenge}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This Month is not supported Yet !")
