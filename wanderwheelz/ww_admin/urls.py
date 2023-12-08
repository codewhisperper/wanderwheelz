# urls.py
from django.urls import path
from .views import admin_login,auth,admin_dashboard
app_name = 'ww_admin'

urlpatterns = [
    path('',admin_login),
    path('login/', admin_login),  
    path('auth/', auth, name='admin_auth'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    
]
    
