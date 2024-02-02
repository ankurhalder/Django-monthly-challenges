import re
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "In january do not eating out meat challenge",
    "february": "In february Walk for at least 20 minutes every day challenge",
    "march": "In march Learn Django for at least 20 minutes every day challenge",
    "april": "In april dance for at least 20 minutes every day challenge",
    "may": "In may exercise for at least 20 minutes every day challenge",
    "june": "In june Read for at least 20 minutes every day challenge",
    "july": "In july Learn NEXT.js for at least 20 minutes every day challenge",
    "august": "In august eat only meat challenge",
    "september": "In september eat only vegetables challenge",
    "october": "In october eat only fruits challenge",
    "november": "In november eat only nuts challenge",
    "december": "In december eat only seeds challenge",
}


# @ Define the URL patterns for the monthly challenges (dynamic URL patterns)
def monthly_challenge(request, month):
    # try:
    challenge_text = monthly_challenges[month]
    response_data = render_to_string("challenges/challenge.html")
    return HttpResponse(response_data)


# except:
#     return HttpResponseNotFound("<h1>This month is not supported!</h1>")


# @ Define a function to handle requests for monthly challenges by number
def monthly_challenges_by_number(
    request,
    number,
):
    sorted_months = list(monthly_challenges.keys())
    if number > len(sorted_months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = sorted_months[number - 1]

    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)
