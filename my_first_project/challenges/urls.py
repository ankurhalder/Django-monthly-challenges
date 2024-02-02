from django.urls import path

from . import views

urlpatterns = [
    # @ Define the URL patterns for the monthly challenges (ststic URL patterns)
    # path("january", views.january),
    # path("february", views.february),
    # path("march", views.march),
    # path("april", views.april),
    # path("may", views.may),
    # path("june", views.june),
    # path("july", views.july),
    # path("august", views.august),
    # path("september", views.september),
    # path("october", views.october),
    # path("november", views.november),
    # path("december", views.december),
    # @ Define the URL patterns for the monthly challenges (dynamic URL patterns)
    path("<month>", views.monthly_challenge),
]
