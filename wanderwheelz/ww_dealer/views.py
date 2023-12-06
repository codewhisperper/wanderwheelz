from django.shortcuts import render
from wanderwheelz.db import *
from django.http import JsonResponse

# Create your views here.

def dealer_login(request):
    return render(request, 'dealer_login.html')

def dealer_register(request):
    return render(request, 'dealer_register.html')

def auth(request):
    email = request.POST['username']
    password = request.POST['password']

    conn = cursor_init()
    with conn.connect() as db_conn:
        query = "SELECT password FROM renter WHERE email = :email"
        results = db_conn.execute(sqlalchemy.text(query), {"email": email}).fetchall()
        fetch_id = "SELECT renter_id FROM renter WHERE password=:password and email=:email"
        res_id = db_conn.execute(sqlalchemy.text(fetch_id), {"password": password,"email": email}).fetchall()
    db_pass = results[0][0]
    
    
    if db_pass == password:
        global id
        id = res_id[0][0]
        print(id)
        return render(request, 'dealer_home.html')
        
    return render(request, 'dealer_login_fail.html')


def registration(request):
    #username = request.POST['username']
    password = request.POST['password']
    mobile = request.POST['mobile']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']

    user = {'password':password, 'phone':mobile, 'first_name':firstname, 'last_name':lastname, 'email':email}
    conn = cursor_init()
    try:
        with conn.connect() as db_conn:
            query = "INSERT INTO renter ( first_name, last_name, email, password, phone) values ( :first_name, :last_name, :email, :password, :phone);"
            db_conn.execute(sqlalchemy.text(query), user)
            db_conn.commit()
    except Exception as err:
        print(err)
        return render(request, 'dealer_register_fail.html')
    return render(request, 'dealer_registered.html')
def ride_review(request):
    car_ride = {
        'model': request.POST['model'],
        'number_plate': request.POST['number_plate'],
        'rate': request.POST['rate'],
        'capacity': request.POST['capacity'],
        'color': request.POST['color'],
        'branch': request.POST['branch'],
        'description': request.POST['description'],
        'city': request.POST['city'],
        'Car_image': request.POST['Car_image'],
        'availability_from': request.POST['availability_from'],
        'availability_to': request.POST['availability_to'],
        'renter_id':id
    }

    conn = cursor_init()
    try:
        with conn.connect() as db_conn:
            query = '''
                INSERT INTO ride (renter_id,availability_from, availability_to, model, number_plate, rate, capacity, color, branch, description, city, Car_image)
                VALUES (:renter_id,:availability_from, :availability_to, :model, :number_plate, :rate, :capacity, :color, :branch, :description, :city, :Car_image)
            '''
            db_conn.execute(sqlalchemy.text(query), car_ride)
            db_conn.commit()

    except Exception as err:
        print(err)

    return render(request, 'ride_template.html')

def verification(request):
    return render(request, 'dealer_verification.html')

def verification_form(request):

    identification = request.POST['identification']
    license = request.POST['license']
    insurance = request.POST['insurance']
    registration = request.POST['registration']

    verify = {
        'Identification': identification,
        'License': license,
        'Insurance': insurance,
        'Registration': registration,
    }
    conn = cursor_init()


    try:
        with conn.connect() as db_conn:
            query = '''
                INSERT INTO renter_verification (identification, license, insurance, registration, verification_status)
                VALUES (:Identification, :License, :Insurance, :Registration, true)
            '''
            db_conn.execute(sqlalchemy.text(query), verify)
            db_conn.commit()

    except Exception as err:
        print(err)
        return render(request,"dealer_register_fail.html")
    try:
        with conn.connect() as db_conn:
            query = '''
                SELECT renter_verification_id FROM renter_verification WHERE license = :License;
            '''
            results = db_conn.execute(sqlalchemy.text(query), {"License": license}).fetchall()
            verification_id = results[0][0]
            id_renter_verification(verification_id,db_conn)
    except Exception as err:
        print(err)
    return render(request,"dealer_verified.html")

def id_renter_verification(ver_id,db_conn):
    query = '''
    UPDATE renter
    SET renter_verification_id = :ver_id
    WHERE renter_id = :id;
    '''
    db_conn.execute(sqlalchemy.text(query), {'ver_id':ver_id,'id':id})
    db_conn.commit()

def dealer_booking(request):
    try:
        conn = cursor_init()
        with conn.connect() as db_conn:
            query = "SELECT * FROM ride where renter_id= :id"
            results=db_conn.execute(sqlalchemy.text(query),{'id':id}).fetchall()
            print(results)
            my_book = []
            for result in results:
                book_dict = {
                    'Model': result[3],
                    'Rate' : result[5],
                    'Capacity' : result[6],
                    'Available_from' : result[10].strftime('%Y-%m-%d %H:%M:%S') if result[4] else None,
                    'Available_to' : result[11].strftime('%Y-%m-%d %H:%M:%S') if result[4] else None
                }
            my_book.append(book_dict)
            print(my_book)
            #request.session['bookings'] = my_book
            return render(request,'dealer_history.html')
    except Exception as e:
        print(e)
        return render(request,'dealer_register_fail.html')
    


            




