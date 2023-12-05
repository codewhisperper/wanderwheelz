import sqlalchemy
from django.shortcuts import render
from wanderwheelz.db import *
from datetime import datetime
from django.contrib import messages

def customer_login(request):
    return render(request, 'customer/customer_login.html')


def customer_logout(request):
    try:
        del request.session['user']
    except:
        return render(request, 'customer/customer_login.html')
    return render(request, 'customer/customer_login.html')


def auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        conn = cursor_init()
        with conn.connect() as db_conn:
            query = "SELECT password, first_name, rentee_id FROM rentee WHERE email = :username"
            results = db_conn.execute(sqlalchemy.text(query), {"username": username}).fetchall()

        db_pass, first_name, user_id = (results[0][0], results[0][1], results[0][2]) if results else (None, None, None)

        if db_pass == password:
            request.session['user'] = first_name
            request.session['user_id'] = user_id
            return get_home(request)
        return render(request, 'customer/customer_login_fail.html')
    return render(request, 'customer/customer_login.html')


def get_home(request):
    try:
        if request.session['user']:
            return render(request, 'customer/customer_home.html')
    except:
        return render(request, 'customer/customer_login.html')


def customer_register(request):
    return render(request, 'customer/customer_register.html')


def registration(request):
    password = request.POST['password']
    mobile = request.POST['mobile']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']

    user = {'password':password, 'phone':mobile, 'first_name':firstname,
            'last_name':lastname, 'email':email}
    conn = cursor_init()
    try:
        with conn.connect() as db_conn:
            query = ("INSERT INTO rentee (first_name, last_name, email, password, phone) "
                     "values (:first_name, :last_name, :email, :password, :phone);")
            db_conn.execute(sqlalchemy.text(query), user)
            db_conn.commit()
    except Exception as err:
        print(err)
        return render(request, 'customer/customer_register_fail.html')
    return render(request, 'customer/customer_registered.html')


def search(request):
    try:
        if request.session['user']:
            return render(request, 'customer/customer_search.html')
    except:
        return render(request, 'customer/customer_login.html')
    return render(request, 'customer/customer_login.html')


def search_results(request):
    try:
        if request.session['user']:
            city = request.POST['city']
            from_date = request.POST.get('from', None)
            to_date = request.POST.get('to', None)

            query_params = {'city': city}

            date_conditions = ""
            if from_date and to_date:
                date_conditions = " AND availability_from <= :from_date AND availability_to >= :to_date"
                query_params['from_date'] = from_date
                query_params['to_date'] = to_date
            elif from_date:
                date_conditions = " AND availability_from <= :from_date AND availability_to >= NOW()"
                query_params['from_date'] = from_date
            elif to_date:
                date_conditions = " AND availability_from <= NOW() AND availability_to >= :to_date"
                query_params['to_date'] = to_date

            conn = cursor_init()

            with conn.connect() as db_conn:
                query = f"SELECT * FROM ride WHERE city = :city AND is_available = True{date_conditions}"
                results = db_conn.execute(sqlalchemy.text(query), query_params).fetchall()

            cars = []
            for result in results:
                car_dict = {
                    'id': result[0],
                    'name': result[3],
                    'rate': int(result[5]),
                    'capacity': result[6],
                    'color': result[7],
                    'description': result[9],
                    'from': result[10].strftime('%Y-%m-%d %H:%M:%S') if result[10] else None,
                    'to': result[11].strftime('%Y-%m-%d %H:%M:%S') if result[11] else None
                }
                cars.append(car_dict)

            request.session['cars'] = cars
            request.session['search'] = {'from': from_date, 'to': to_date, 'city': city}

            return render(request, 'customer/customer_search_results.html')
    except:
        return render(request, 'customer/customer_login.html')
    return render(request, 'customer/customer_login.html')


def confirm(request):
    try:
        if request.session['user']:
            id = request.POST['id']
            id = {'id': id}

            conn = cursor_init()
            with conn.connect() as db_conn:
                query = 'SELECT * FROM ride WHERE ride_id = :id'
                result = db_conn.execute(sqlalchemy.text(query), id).fetchall()
            result = result[0]
            car = {
                'id': result[0],
                'name': result[3],
                'rate': int(result[5]),
                'capacity': result[6],
                'description': result[9],
                'from': result[10],
                'to': result[11]}
            return render(request, 'customer/booking_confirmation.html', {'car': car})
    except:
        return render(request, 'customer/customer_login.html')


def book(request):
    try:
        if request.session['user']:
            id = request.POST['id']
            user_id = request.POST['user_id']
            name = request.POST['bname']

            booking = {'ride_id': id, 'rentee_id': user_id, 'name': name, 'date': datetime.now()}
            id = {'id': id}

            conn = cursor_init()
            with conn.connect() as db_conn:
                query = "UPDATE ride SET is_available = False WHERE ride_id = :id"
                db_conn.execute(sqlalchemy.text(query), id)

                query = "INSERT INTO rental (ride_id, rentee_id, rental_name, date) VALUES (:ride_id, :rentee_id, :name, :date)"
                db_conn.execute(sqlalchemy.text(query), booking)
                db_conn.commit()
            return render(request, 'customer/booking_confirmed.html')
    except Exception as err:
        print(err)
        return render(request, 'customer/customer_login.html')


def bookings(request):
    try:
        if request.session['user']:
            id = request.session['user_id']
            id = {"id": id}
            conn = cursor_init()
            with conn.connect() as db_conn:
                query = "SELECT * FROM rental where rentee_id = :id"
                results = db_conn.execute(sqlalchemy.text(query), id).fetchall()

            my_book = []
            for result in results:
                book_dict = {
                    'booking_name': result[3],
                    'date_of_booking': result[4].strftime('%Y-%m-%d %H:%M:%S') if result[4] else None,
                }
                my_book.append(book_dict)
            request.session['bookings'] = my_book
            return render(request, 'customer/customer_bookings.html')
    except Exception as err:
        return render(request, 'customer/customer_login.html')


def manage(request):
    try:
        if request.session['user']:
            return render(request, 'customer/customer_manage.html')
    except:
        return render(request, 'customer/customer_login.html')


def update(request):
    try:
        if request.session['user']:
            old_password = request.POST['old_password']
            user = {'id': request.session['user_id']}

            update_query = 'UPDATE rentee SET '
            if request.POST['new_password']:
                new_password = request.POST['new_password']
                user['password'] = new_password
                update_query += 'password = :password, '
            if request.POST['mobile']:
                mobile = request.POST['mobile']
                user['phone'] = mobile
                update_query += 'phone = :phone, '
            if request.POST['email']:
                email = request.POST['email']
                user['email'] = email
                update_query += 'email = :email, '

            update_query = update_query[:-2]
            update_query += ' WHERE rentee_id = :id'

            conn = cursor_init()
            with conn.connect() as db_conn:
                query = "SELECT password FROM rentee WHERE rentee_id = :id"
                results = db_conn.execute(sqlalchemy.text(query), {"id": request.session['user_id']}).fetchall()
                if results[0][0] == old_password:
                    if len(user) > 1:
                        db_conn.execute(sqlalchemy.text(update_query), user)
                        db_conn.commit()
            messages.success(request, "Information successfully edited!")
            return render(request, 'customer/customer_manage.html')
    except Exception as err:
        print(err)
        return render(request, 'customer/customer_login.html')


def verify(request):
    try:
        if request.session['user']:
            return render(request, 'customer/customer_verification.html')
    except Exception as err:
        print(err)
        return render(request, 'customer/customer_login.html')


def verification(request):
    try:
        if request.session['user']:
            id = request.POST['id']
            ver = {'id': id}
            conn = cursor_init()
            with conn.connect() as db_conn:
                query = "SELECT * FROM rentee_verification WHERE rentee_verification_id = :id"
                result = db_conn.execute(sqlalchemy.text(query), ver).fetchall()
                if len(result) > 0:
                    update_query = 'UPDATE rentee_verification SET '
                    if request.POST['dl']:
                        dl = request.POST['dl']
                        ver['dl'] = dl
                        update_query += 'license = :dl, '
                    if request.POST['insurance']:
                        insurance = request.POST['insurance']
                        ver['insurance'] = insurance
                        update_query += 'insurance = :insurance, '
                    if request.POST['ident']:
                        iden = request.POST['ident']
                        ver['iden'] = iden
                        update_query += 'identification = :iden, '

                    update_query = update_query[:-2]
                    update_query += ' WHERE rentee_verification_id = :id'
                    db_conn.execute(sqlalchemy.text(update_query), ver)
                else:
                    ver = {'id': id, 'iden': request.POST['ident'], 'insurance': request.POST['insurance'],
                           'dl': request.POST['dl']}
                    query = ("INSERT INTO rentee_verification (rentee_verification_id, identification, license, "
                             "insurance, verification_status) values (:id, :iden, :dl, :insurance, 0);")
                    db_conn.execute(sqlalchemy.text(query), ver)
                db_conn.commit()
            messages.success(request, "Verification information successfully added!")
            return render(request, 'customer/customer_verification.html')
    except Exception as err:
        print(err)
        return render(request, 'customer/customer_register_fail.html')