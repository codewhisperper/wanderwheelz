from django.urls import path

from ww_dealer.views import *

urlpatterns = [
    path('dealer_login/', dealer_login)
]
