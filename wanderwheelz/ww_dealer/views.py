from django.shortcuts import render

# Create your views here.


def dealer_login(request):
    return render(request, "dealer/dealer_home.html")
