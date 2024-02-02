from django.urls import path

from . import views

urlpatterns = [
    path("january", views.index),
    path("february", views.index),
    path("march", views.index),
    path("april", views.index),
    path("may", views.index),
    path("june", views.index),
    path("july", views.index),
    path("august", views.index),
    path("september", views.index),
    path("october", views.index),
    path("november", views.index),
    path("december", views.index),
]
