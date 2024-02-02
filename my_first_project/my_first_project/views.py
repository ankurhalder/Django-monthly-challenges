from django.shortcuts import render
from challenges.views import monthly_challenges
from django.http import HttpResponse


# def all_months(request):
#     months_list = list(monthly_challenges.keys())
#     response = "<ul>"
#     for month in months_list:
#         month_path = f"/challenges/{month}"
#         response += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'
#     response += "</ul>"
#     return HttpResponse(response)
def all_months(request):
    months = list(monthly_challenges.keys())

    return render(
        request,
        "challenges/index.html",
        {
            "months": months,
        },
    )
