# views.py
from django.shortcuts import render, redirect
from django.contrib import messages

def admin_login(request):
    return render(request, 'login.html')




# def admin_dashboard(request):
#     # Implement your admin dashboard logic here
#     return render(request, 'admin/dashboard.html')  # Create a dashboard.html template
