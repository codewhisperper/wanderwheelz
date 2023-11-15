from django.shortcuts import render
from ww_customer import *


def home(request):
    return render(request, "home/home.html")
