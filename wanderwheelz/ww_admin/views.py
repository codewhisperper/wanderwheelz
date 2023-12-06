# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from wanderwheelz.db import cursor_init
from django.http import HttpResponse
import sqlalchemy  # Added import for SQLAlchemy

def admin_login(request):
    """
    Renders the admin login page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered login.html template.
    """
    return render(request, 'login.html')


def auth(request):
    """
    Handles user authentication.

    If the request method is POST, it attempts to authenticate the user
    by checking the provided username and password against the admin table in the database.
    If authentication is successful, the user is redirected to the admin dashboard.
    If authentication fails, an error message is displayed.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to admin_dashboard on successful authentication.
                      Renders login_fail.html with an error message on authentication failure.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Initialize database connection
        conn = cursor_init()

        # Connect to the database and execute the authentication query
        with conn.connect() as db_conn:
            query = "SELECT password FROM admin WHERE username = :username"
            results = db_conn.execute(sqlalchemy.text(query), {"username": username}).fetchall()

        # Debug print for results
        print("Results:", results)

        # Check if authentication was successful
        if results:
            db_pass = results[0][0]
            if db_pass == password:
                return redirect('ww_admin:admin_dashboard')

        # Debug print for authentication failure
        print("Authentication failed.")
        messages.error(request, 'Invalid username or password')
        return render(request, 'login_fail.html')

    return redirect('ww_admin:admin_login')


def admin_dashboard(request):
    """
    Renders the admin dashboard page with data fetched from the ride_review table.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered dashboard.html template with ride review data.
    """
    # Fetch data from the ride_review table using SQLAlchemy
    conn = cursor_init()
    with conn.connect() as db_conn:
        query = "SELECT * FROM ride_review"
        results = db_conn.execute(sqlalchemy.text(query)).fetchall()

    # Prepare context for rendering the template
    context = {
        'dashboard_data': results,
    }

    return render(request, 'dashboard.html', context)
