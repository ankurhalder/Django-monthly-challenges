import re
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")


# @ Define a function to handle requests for monthly challenges by number
def monthly_challenges_by_number(
    request,
    number,
):
    # Create a list of sorted months from the keys of the monthly_challenges dictionary
    sorted_months = list(monthly_challenges.keys())

    # Check if the provided number is greater than the number of months
    if number > len(sorted_months):
        # If the number is invalid, return a 404 Not Found response
        return HttpResponseNotFound("Invalid month")

    # Calculate the index of the redirect month in the sorted_months list
    redirect_month = sorted_months[number - 1]

    # Redirect the user to the URL for the corresponding monthly challenge
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)
