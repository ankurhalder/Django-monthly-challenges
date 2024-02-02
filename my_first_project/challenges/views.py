import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# @ Define the URL patterns for the monthly challenges (ststic URL patterns)
def january(request):
    return HttpResponse("In january do not eating out meat challenge")


def february(request):
    return HttpResponse("In february Walk for at least 20 minutes every day challenge")


def march(request):
    return HttpResponse(
        "In march Learn Django for at least 20 minutes every day challenge"
    )


def april(request):
    return HttpResponse("In april dance for at least 20 minutes every day challenge")


def may(request):
    return HttpResponse("In may exercise for at least 20 minutes every day challenge")


def june(request):
    return HttpResponse("In june Read for at least 20 minutes every day challenge")


def july(request):
    return HttpResponse(
        "In july Learn NEXT.js for at least 20 minutes every day challenge"
    )


def august(request):
    return HttpResponse("In august eat only meat challenge")


def september(request):
    return HttpResponse("In september eat only vegetables challenge")


def october(request):
    return HttpResponse("In october eat only fruits challenge")


def november(request):
    return HttpResponse("In november eat only nuts challenge")


def december(request):

    return HttpResponse("In december eat only seeds challenge")


# @ Define the URL patterns for the monthly challenges (dynamic URL patterns)
def monthly_challenge(request, month):
    if month == "january":
        challenge_text = "In january do not eating out meat challenge"
    elif month == "february":
        challenge_text = "In february Walk for at least 20 minutes every day challenge"
    elif month == "march":
        challenge_text = (
            "In march Learn Django for at least 20 minutes every day challenge"
        )
    elif month == "april":
        challenge_text = "In april dance for at least 20 minutes every day challenge"
    elif month == "may":
        challenge_text = "In may exercise for at least 20 minutes every day challenge"
    elif month == "june":
        challenge_text = "In june Read for at least 20 minutes every day challenge"
    elif month == "july":
        challenge_text = (
            "In july Learn NEXT.js for at least 20 minutes every day challenge"
        )
    elif month == "august":
        challenge_text = "In august eat only meat challenge"
    elif month == "september":
        challenge_text = "In september eat only vegetables challenge"
    elif month == "october":
        challenge_text = "In october eat only fruits challenge"
    elif month == "november":
        challenge_text = "In november eat only nuts challenge"
    elif month == "december":
        challenge_text = "In december eat only seeds challenge"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
