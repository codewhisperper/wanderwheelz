from django.shortcuts import render
from wanderwheelz.db import *

def customer_login(request):
    return render(request, 'customer/customer_login.html')

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username)
    print(password)
    conn = cursor_init()
    with conn.connect() as db_conn:
        results = db_conn.execute(sqlalchemy.text("SELECT * FROM test")).fetchall()
    print(results)
    return None