from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


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
