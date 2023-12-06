from django.urls import path

from ww_dealer.views import *

urlpatterns = [
    path('dealer_login/', dealer_login),
    path('dealer_register/',dealer_register),
    path('auth/', auth),
    path('registration/', registration),
    path('create_ride/', ride_review),
    path('verification/',verification),
    path('history/',dealer_booking),
    path('verification_form/',verification_form)

]
