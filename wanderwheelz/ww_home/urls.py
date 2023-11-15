from django.urls import path
from ww_home.views import *
from ww_customer import *
from ww_dealer import *

urlpatterns = [
    path('', home)
]
