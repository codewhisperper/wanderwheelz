from django.shortcuts import render
from wanderwheelz.db import *


def customer_login(request):
    return render(request, 'customer/customer_login.html')


def auth(request):
    username = request.POST['username']
    password = request.POST['password']

    conn = cursor_init()
    with conn.connect() as db_conn:
        query = "SELECT password FROM rentee WHERE username = :username"
        results = db_conn.execute(sqlalchemy.text(query), {"username": username}).fetchall()

    db_pass = results[0][0]

    if db_pass == password:
        return render(request, 'customer/customer_home.html')
    return render(request, 'customer/customer_login_fail.html')


def customer_register(request):
    return render(request, 'customer/customer_register.html')

def registration(request):
    username = request.POST['username']
    password = request.POST['password']
    mobile = request.POST['mobile']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']

    user = {'username':username, 'password':password, 'phone':mobile, 'first_name':firstname, 'last_name':lastname, 'email':email, 'status':'Active'}
    conn = cursor_init()
    try:
        with conn.connect() as db_conn:
            query = "INSERT INTO rentee (username, first_name, last_name, email, password, phone, status) values (:username, :first_name, :last_name, :email, :password, :phone, :status);"
            db_conn.execute(sqlalchemy.text(query), user)
            db_conn.commit()
    except Exception as err:
        print(err)
        return render(request, 'customer/customer_register_fail.html')
    return render(request, 'customer/customer_registered.html')