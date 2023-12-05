# urls.py
from django.urls import path
from .views import admin_login

app_name = 'ww_admin'

urlpatterns = [
    #path('login/', auth ),
    path('',admin_login)
    # path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    # Add other URLs as needed
]
