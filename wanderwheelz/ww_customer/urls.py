from django.urls import path

from ww_customer.views import *

urlpatterns = [
    path('customer_login/', customer_login),
    path('auth/', auth),
    path('customer_register/', customer_register),
    path('registration/', registration),
    path('search/', search),
    path('search_results/', search_results),
    path('confirm/', confirm),
    path('customer_logout/', customer_logout),
    path('book/', book),
    path('my_bookings/', bookings),
    path('customer_manage/', manage),
    path('update_user/', update),
    path('verify_user/', verify),
    path('verification/', verification),
    path('home/', get_home),
]
