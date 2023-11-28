from django.urls import path

from ww_customer.views import *

urlpatterns = [
    path('customer_login/', customer_login),
    path('auth/', auth),
    path('customer_register/', customer_register),
    path('registration/', registration),
]