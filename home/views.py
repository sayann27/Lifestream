from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from home.models import Hospital, Receiver, Donor, Donation, Receiving, Blood_group, City
from home.functions import *
from datetime import datetime, date
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

# Create your views here.

def index(requests):
    return render(requests, 'index.html')

def about(requests):
    return render(requests, 'about.html')

def venues(requests):
    return render(requests, 'venues.html')

def login(requests):
    return render(requests, 'login.html')

def register(requests):
    context  ={}
    context['display'] = "none"
    if requests.method == "POST":
        user_type = requests.POST.get('user_type')
        if user_type != "Hospital":
            dob = requests.POST.get('dob')
            bg = requests.POST.get('bg')

        if user_type == "Hospital":
            cover_image = requests.POST.get('image')

        name = requests.POST.get('name')
        email = requests.POST.get('email')    
        phone = requests.POST.get('phone')
        addline1 = requests.POST.get('addline1')
        addline2 = requests.POST.get('addline2')
        city = requests.POST.get('city')
        state = requests.POST.get('state')
        pincode = requests.POST.get('pincode')
        pwd = requests.POST.get('pwd')
        pwd1 = requests.POST.get('pwd1')
        check1 = requests.POST.get('check1')
        if not check_email(email):
            messages.warning(requests, "Enter the email correctly")
            return render(requests, "register.html", context)
        elif not check_phone(phone):
            messages.warning(requests, "Enter the Phone number correctly")
            return render(requests, "register.html", context)
        elif not check_pin(pincode):
            messages.warning(requests, "Enter the pincode correctly")
            return render(requests, "register.html", context)
        elif not pwd == pwd1:
            messages.warning(requests, "The passwords do not match")
            return render(requests, "register.html", context)
        elif not check1:
            messages.warning(requests, "Please agree with the terms and conditions")
            return render(requests, "register.html", context)
        existing = User.objects.filter(username = email)
        if len(existing) > 0:
            messages.warning(requests, "The user already exists")
            return render(requests, "register.html", context)
        user = User.objects.create_user(username = name, email=email, password=pwd)
        user.username = email
        user.first_name = name
        user.save()
        if user_type == "Receiver":
            registration = Receiver(name = name, email = email, dob = dob, phone = phone, bg = bg, addline1=addline1, addline2=addline2, city=city, state=state, pincode=pincode, pwd=pwd )
        elif user_type == "Donor":
            registration = Donor(name = name, email = email, dob = dob, phone = phone, bg = bg, addline1=addline1, addline2=addline2, city=city, state=state, pincode=pincode, pwd=pwd )
        else:
            registration = Hospital(name=name, email=email, phone=phone, addline1=addline1, addline2=addline2, city=city, state=state, pincode=pincode, pwd=pwd, cover_image = cover_image)
            blood = Blood_group(hosp_email=email)
            blood.save()
        registration.save()
        return render(requests, 'reg_successful.html')

    return render(requests, 'register.html', context)

def hospital_login(requests):
    if requests.method == "POST":
        print("reading")
        email = requests.POST.get('email')
        pwd = requests.POST.get('pwd')
        user = authenticate(requests, username = email, password = pwd)
        if user is None:
            messages.warning(requests, "User doesn't exist")
            return redirect("hospital_login")
        datas = Hospital.objects.filter(email = email, pwd = pwd).first()
        requests.session['username'] = datas.name
        requests.session['user_city'] = datas.city
        requests.session['email'] = email
        requests.session['type_user'] = "hospital"
        check = requests.POST.get('check1')
        if user is not None:
            login(requests)
            if check:
                response = redirect('dashboard_hospital')
                response.set_cookie('keep', True, max_age=None)
                response.set_cookie('user_t', "Hospital", max_age=None)
                return response
            else:
                return redirect('dashboard_hospital')
        else:
            print("Wrong information")
            return redirect('hospital_login')
    if requests.COOKIES.get('keep', None)  and requests.COOKIES.get('user_t', None) == "Hospital":
        print("Logged in")
        return redirect('dashboard_hospital')
    else:
        print("Not logged in")
        context = {
            "user_name":"hospital",
        }
        return render(requests, 'sign_in.html', context)

def receiver_login(requests):
    if requests.method == "POST":
        print("reading")
        email = requests.POST.get('email')
        pwd = requests.POST.get('pwd')
        user = authenticate(requests, username = email, password = pwd)
        if user is None:
            messages.warning(requests, "User doesn't exist")
            return redirect("receiver_login")
        datas = Receiver.objects.filter(email = email, pwd = pwd).first()
        requests.session['username'] = datas.name
        requests.session['user_city'] = datas.city
        requests.session['email'] = email
        requests.session['type_user'] = "receiver"
        check = requests.POST.get('check1')
        if user is not None:
            login(requests)
            if check:
                response = redirect('dashboard_receiver')
                response.set_cookie('keep', True, max_age=None)
                response.set_cookie('user_t', "Receiver", max_age=None)
                return response
            else:
                return redirect('dashboard_receiver')
        else:
            print("Wrong information")
            return redirect('receiver_login')
    if requests.COOKIES.get('keep', None)  and requests.COOKIES.get('user_t', None) == "Receiver":
        print("Logged in")
        return redirect('dashboard_receiver')
    else:
        print("Not logged in")
        context = {
            "user_name":"receiver",
        }
        return render(requests, 'sign_in.html', context)

def donor_login(requests):
    if requests.method == "POST":
        email = requests.POST.get('email')
        pwd = requests.POST.get('pwd')
        user = authenticate(requests, username = email, password = pwd)
        checking = Donor.objects.filter(email = email, pwd = pwd)
        if user is None:
            messages.warning(requests, "User doesn't exist")
            return redirect("donor_login")
        elif len(checking) == 0:
            messages.warning(requests, "User doesn't exist")
            return redirect("donor_login")
        datas = Donor.objects.filter(email = email, pwd = pwd)[0]
        # print(datas.city_ID.name)
        requests.session['username'] = datas.name
        requests.session['user_city'] = datas.city_ID.name
        requests.session['email'] = email
        requests.session['type_user'] = "donor"
        check = requests.POST.get('check1')
        # if check:
        #     requests.set_cookie('keep', True)
        if user is not None:
            login(requests)
            if check:
                response = redirect('dashboard_donor')
                response.set_cookie('keep', True, max_age=None)
                response.set_cookie('user_t', "Donor", max_age=None)
                return response
            else:
                return redirect('dashboard_donor')
        # datas = Donor.objects.all().filter(email=email, pwd=pwd)
        # for data in datas:
        #     if data.email == email and data.pwd == pwd:
        #         context = {
        #             "username" :data.name,
        #         }
        #         user_name = data.name
        #         user_city = data.city
        #         requests.session['username'] = data.name
        #         requests.session['user_city'] = data.city
        #         requests.session.set_expiry(300)
        #         return dashboard_donor(requests, user_city, user_name)

        #     else: 
        #         return HttpResponse("Error occured")
        else:
            print("Wrong information")
            return redirect('donor_login')
    if requests.COOKIES.get('keep', None) and requests.COOKIES.get('user_t', None) == "Donor" :
        print("Logged in")
        return redirect('dashboard_donor')
    else:
        print("Not logged in")
        context = {
            "user_name":"donor",
        }
        return render(requests, 'sign_in.html', context)

def dashboard_receiver(requests):
    context = {}
    context['username'] = requests.session['username']
    hospital_name = Hospital.objects.filter(city_ID = City.objects.filter(name=requests.session['user_city'])[0].id)
    number = len(hospital_name)
    if number >= 3:
        for n in range(0,3):
            context['hospitalName' + str(n+1)] = hospital_name[n].name
            context['hospital_location' + str(n+1)] = hospital_name[n].addline1+ " " +hospital_name[n].addline2 + ", " +hospital_name[n].city + " "+ str(hospital_name[n].pincode),
            context['image' + str(n+1)] = change_link(hospital_name[n].cover_image)
            context['visibility' + str(n+1)] = "block"
    elif number <3:
        for n in range(0,number):
            context['hospitalName' + str(n+1)] = hospital_name[n].name
            context['hospital_location' + str(n+1)] = hospital_name[n].addline1+ " " +hospital_name[n].addline2 + ", " +hospital_name[n].city + " "+ str(hospital_name[n].pincode),
            context['image' + str(n+1)] = change_link(hospital_name[n].cover_image)
            context['visibility' + str(n+1)] = "block"


    if number < 3:
        for n in range(number, 4):
            context['visibility' + str(n+1)] = "none"

    return render(requests, 'dashboard_receiver.html', context)

def dashboard_donor(requests):
    hospital_name = Hospital.objects.filter(city_ID = City.objects.filter(name=requests.session['user_city'])[0].id)
    number = len(hospital_name)
        
    
    context = {}
    context['username'] = requests.session['username']
    if number >= 3:
        for n in range(0,3):
            context['hospitalName' + str(n+1)] = hospital_name[n].name
            context['hospital_location' + str(n+1)] = hospital_name[n].addline1+ " " +hospital_name[n].addline2 + ", " +hospital_name[n].city + " "+ str(hospital_name[n].pincode),
            context['image' + str(n+1)] = change_link(hospital_name[n].cover_image)
            context['visibility' + str(n+1)] = "block"
    elif number <3:
        for n in range(0,number):
            context['hospitalName' + str(n+1)] = hospital_name[n].name
            context['hospital_location' + str(n+1)] = hospital_name[n].addline1+ " " +hospital_name[n].addline2 + ", " +hospital_name[n].city + " "+ str(hospital_name[n].pincode),
            context['image' + str(n+1)] = change_link(hospital_name[n].cover_image)
            context['visibility' + str(n+1)] = "block"


    if number < 3:
        for n in range(number, 4):
            context['visibility' + str(n+1)] = "none"
            


    return render(requests, 'dashboard_donor.html', context)



def logout_view(requests):
    logout(requests)
    if requests.COOKIES.get('keep', None):
        response = render(requests, 'logout.html')
        response.delete_cookie('keep')
        response.delete_cookie('user_t')
        return response
    else:
        return render(requests, 'logout.html')


def donate(requests):
    context = {}
    hospital_name = Hospital.objects.filter(city_ID = City.objects.filter(name=requests.session['user_city'])[0].id)
    name_list = []
    for i in range(len(hospital_name)):
        name_list.append(hospital_name[i].name)
    
    context['name_list'] = name_list
    context['length'] = len(hospital_name)
    if requests.method == "POST":
        hosp_name = requests.POST.get('hosp_name')
        email = requests.POST.get('email')
        time = requests.POST.get('time')
        date = requests.POST.get('date')
        donor_name = requests.session['username']
        city_ID = City.objects.filter(name=requests.session['user_city'])[0].id
        donate = Donation(donor_name=donor_name, hosp_name=hosp_name, hosp_email=email, time=time,date=date,  city_ID=city_ID, status="Not donated")
        donate.save()
        messages.success(requests, "Request sent to hospital successfully")


    return render(requests, 'donor_donate.html', context)


def my_donations(requests):
    donations = Donation.objects.filter(status="Not donated", donor_name=requests.session['username']) | Donation.objects.filter(status= "Accepted", donor_name=requests.session['username'])
    donations_prev = Donation.objects.filter(status = "Donated", donor_name=requests.session['username']) | Donation.objects.filter(status="Rejected", donor_name=requests.session['username'])
    context = {}
    don_active_list = []
    don_prev_list = []
    for i in range(len(donations)):
        date = donations[i].date
        time = donations[i].time
        don_active_list.append([donations[i].hosp_name, date.strftime("%m/%d/%Y"), time.strftime("%H:%M:%S"), donations[i].status])


    for i in range(len(donations_prev)):
        date = donations_prev[i].date
        time = donations_prev[i].time
        don_prev_list.append([donations_prev[i].hosp_name, date.strftime("%m/%d/%Y"), time.strftime("%H:%M:%S"), donations_prev[i].status])


    # print(don_prev_list)
    # print(don_list)
    context['donations_list'] = don_active_list
    context['active_length'] = len(donations)
    context['donations_prev'] = don_prev_list
    context['prev_length'] = len(donations_prev)
    # print(len(donations))

    return render(requests, 'my_donations.html', context)

def medical_records(requests):
    context = {}
    if requests.session['type_user'] == "receiver":
        context['navbar'] = 'dash_nav_receiver.html'
        records = Receiver.objects.filter(email=requests.session['email']).exclude(medical_records="None")
        user = Receiver.objects.filter(email = requests.session['email'])
    else:
        records = Donor.objects.filter(email= requests.session['email']).exclude(medical_records="None")
        user = Donor.objects.filter(email = requests.session['email'])
        context['navbar'] = 'dash_nav_donor.html'
    context['type_user'] = requests.session['type_user']
    context['length'] = len(records)
    print(len(records))
    if len(records) >0:
        context['record_link'] = change_link(records[0].medical_records)
        print(records[0].medical_records)
    if requests.method == "POST":
        record = requests.POST.get('recordss')
        user.update(medical_records=record)
        

    return render(requests, 'medical_records_donor.html', context)

def hospital_list(requests):
    context = {}
    if requests.session['type_user'] == "receiver":
        context['navbar'] = 'dash_nav_receiver.html'
    else:
        context['navbar'] = 'dash_nav_donor.html'

    hospitals = Hospital.objects.filter(city= requests.session['user_city'])
    context['length'] = len(hospitals)
    hosp_list = []
    for i in range(len(hospitals)):
        location = hospitals[i].addline1+ " " +hospitals[i].addline2 + ", " +hospitals[i].city + " "+ str(hospitals[i].pincode)
        name = hospitals[i].name
        hosp_list.append([name, location])
    
    context['hosp'] = hosp_list
    return render(requests, 'hospital_list.html', context)

def my_receivings(requests):
    receivings = Receiving.objects.filter(status="Not received", receiver_name=requests.session['username']) | Receiving.objects.filter(status="Accepted", receiver_name=requests.session['username'])
    receivings_prev = Receiving.objects.filter(status = "Received", receiver_name=requests.session['username']) | Receiving.objects.filter(status="Rejected", receiver_name=requests.session['username'])
    context = {}
    rec_active_list = []
    rec_prev_list = []
    for i in range(len(receivings)):
        date = receivings[i].date
        time = receivings[i].time
        rec_active_list.append([receivings[i].hosp_name, date.strftime("%m/%d/%Y"), time.strftime("%H:%M:%S"), receivings[i].status])


    for i in range(len(receivings_prev)):
        date = receivings_prev[i].date
        time = receivings_prev[i].time
        rec_prev_list.append([receivings_prev[i].hosp_name, date.strftime("%m/%d/%Y"), time.strftime("%H:%M:%S"), receivings_prev[i].status])


    # print(don_prev_list)
    # print(don_list)
    context['receivings_list'] = rec_active_list
    context['active_length'] = len(receivings)
    context['receivings_prev'] = rec_prev_list
    context['prev_length'] = len(receivings_prev)
    return render(requests, 'my_receivings.html', context)

def receive(requests):
    context = {}
    hospital_name = Hospital.objects.filter(city = requests.session['user_city'])
    name_list = []
    for i in range(len(hospital_name)):
        name_list.append(hospital_name[i].name)
    
    context['name_list'] = name_list
    context['length'] = len(hospital_name)
    if requests.method == "POST":
        hosp_name = requests.POST.get('hosp_name')
        email = requests.POST.get('email')
        time = requests.POST.get('time')
        date = requests.POST.get('date')
        donor_name = requests.session['username']
        city = requests.session['user_city']
        receive = Receiving(receiver_name=donor_name, hosp_name=hosp_name, hosp_email=email, time=time,date=date,  city=city, status="Not received")
        receive.save()
        messages.success(requests, "Request sent to hospital successfully")
    return render(requests, 'receive.html', context)

def dashboard_hospital(requests):
    hospitals = Hospital.objects.filter(email=requests.session['email'])[0]
    context = {}
    context['image'] = change_link(hospitals.cover_image)
    donations = Donation.objects.filter(hosp_name=requests.session['username'], status="Donated")
    receiver = Receiving.objects.filter(hosp_name=requests.session['username'], status="Received")
    blood = Blood_group.objects.filter(hosp_email=requests.session['email'])[0]
    count = blood.Apos + blood.Aneg + blood.Bpos + blood.Bneg + blood.Opos + blood.Oneg + blood.ABpos + blood.ABneg
    context['donations'] = len(donations)
    context['receivers'] = len(receiver)
    context['count'] = count
    return render(requests, 'dashboard_hospital.html', context)

def hosp_blood(requests):
    context = {}
    if requests.method == "POST":
        blood_data = Blood_group.objects.filter(hosp_email=requests.session['email'])
        if requests.POST.get('Apos') != '':
            blood_data.update(Apos=requests.POST.get('Apos'))
        if requests.POST.get('Aneg') != '':
            blood_data.update(Aneg=requests.POST.get('Aneg'))
        if requests.POST.get('Bpos') != '':
            blood_data.update(Bpos=requests.POST.get('Bpos'))
        if requests.POST.get('Bneg') != '':
            blood_data.update(Bneg=requests.POST.get('Bneg'))
        if requests.POST.get('Opos') != '':
            blood_data.update(Opos=requests.POST.get('Opos'))
        if requests.POST.get('Oneg') != '':
            blood_data.update(Oneg=requests.POST.get('Oneg'))
        if requests.POST.get('ABpos') != '':
            blood_data.update(ABpos=requests.POST.get('ABpos'))
        if requests.POST.get('ABneg') != '':
            blood_data.update(ABneg=requests.POST.get('ABneg'))
        
    return render(requests, 'hosp_blood.html', context)


def hosp_info(requests):
    context = {}
    blood = Blood_group.objects.filter(hosp_email=requests.session['email'])
    groups = ["Apos", "Aneg", "Bpos", "Bneg", "ABpos", "ABneg", "Opos", "Oneg"]
    context['length'] = len(blood)
    hosp = [["A+", blood[0].Apos], ["A-", blood[0].Aneg], ["B+", blood[0].Bpos], ["B-", blood[0].Bneg], ["AB+", blood[0].ABpos], ["AB-", blood[0].ABneg], ["O+", blood[0].Opos], ["O-", blood[0].Oneg]]
    context['hosp'] = hosp
    return render(requests, 'hosp_info.html', context)

def hosp_donors(requests):
    context = {}
    donations = Donation.objects.filter(hosp_email=requests.session['email'], status="Donated")
    hosp = []
    for i in range(len(donations)):
        name = donations[i].donor_name
        bg = Donor.objects.filter(name=name)[0].bg
        hosp.append([name, bg])
    context['hosp'] = hosp
    context['length'] = len(donations)
    return render(requests, 'hosp_donors.html', context)


def hosp_receivers(requests):
    context = {}
    receivings = Receiving.objects.filter(hosp_email=requests.session['email'], status="Received")
    hosp = []
    for i in range(len(receivings)):
        name = receivings[i].receiver_name
        bg = Receiver.objects.filter(name=name)[0].bg
        hosp.append([name, bg])
    context['hosp'] = hosp
    context['length'] = len(receivings)
    return render(requests, 'hosp_receivers.html', context)

def donor_requests(requests):
    context = {}
    donors = Donation.objects.filter(status="Not donated", hosp_email=requests.session['email'])
    req_list = []
    for i in range(len(donors)):
        name = donors[i].donor_name
        bg = Donor.objects.filter(name=name)[0].bg
        dob = Donor.objects.filter(name=name)[0].dob
        age = date.today().year - dob.year - ((date.today().month, date.today().day) < (dob.month, dob.day))
        date_rec = donors[i].date
        time_rec = donors[i].time
        req_list.append([["Name", name], ["Blood Group", bg], ["Age", age], ["Date", date_rec], ["Time", time_rec]])
    
    context['req_list'] = req_list
    if requests.method == "POST":
        for i in range(len(req_list)):
            if requests.POST.get('checkbox' + str(i)) == "":
                Donation.objects.filter(donor_name=donors[i].donor_name, hosp_email=requests.session['email']).update(status = "Accepted")
            
        return redirect('donor_requests')
        
    return render(requests, 'donor_requests.html', context)

def accepted_requests(requests):
    context = {}
    donors = Donation.objects.filter(status="Accepted", hosp_email=requests.session['email'])
    req_list = []
    for i in range(len(donors)):
        name = donors[i].donor_name
        bg = Donor.objects.filter(name=name)[0].bg
        dob = Donor.objects.filter(name=name)[0].dob
        age = date.today().year - dob.year - ((date.today().month, date.today().day) < (dob.month, dob.day))
        date_rec = donors[i].date
        time_rec = donors[i].time
        req_list.append([["Name", name], ["Blood Group", bg], ["Age", age], ["Date", date_rec], ["Time", time_rec]])
        
    
    context['req_list'] = req_list
    if requests.method == "POST":
        for i in range(len(req_list)):
            if requests.POST.get('checkbox' + str(i)) == "":
                Donation.objects.filter(donor_name=donors[i].donor_name, hosp_email=requests.session['email']).update(status = "Donated")
                if Donor.objects.filter(name=donors[i].donor_name)[0].bg == "A+":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].Apos
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(Apos=quant+1)
                elif Donor.objects.filter(name=donors[i].donor_name)[0].bg == "A-":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].Aneg
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(Aneg=quant+1)
                elif Donor.objects.filter(name=donors[i].donor_name)[0].bg == "B+":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].Bpos
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(Bpos=quant+1)
                elif Donor.objects.filter(name=donors[i].donor_name)[0].bg == "B-":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].Bneg
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(Bneg=quant+1)
                elif Donor.objects.filter(name=donors[i].donor_name)[0].bg == "AB+":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].ABpos
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(ABpos=quant+1)
                elif Donor.objects.filter(name=donors[i].donor_name)[0].bg == "AB-":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].ABneg
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(ABneg=quant+1)
                elif Donor.objects.filter(name=donors[i].donor_name)[0].bg == "O+":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].Opos
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(Opos=quant+1)
                elif Donor.objects.filter(name=donors[i].donor_name)[0].bg == "O-":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].Oneg
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(Oneg=quant+1)
        # return redirect('accepted_requests')
    else:
        return render(requests, 'accepted_requests.html', context)


def receiver_requests(requests):
    context = {}
    receivers = Receiving.objects.filter(status="Not received", hosp_email=requests.session['email'])
    req_list = []
    for i in range(len(receivers)):
        name = receivers[i].receiver_name
        bg = Receiver.objects.filter(name=name)[0].bg
        dob = Receiver.objects.filter(name=name)[0].dob
        age = date.today().year - dob.year - ((date.today().month, date.today().day) < (dob.month, dob.day))
        date_rec = receivers[i].date
        time_rec = receivers[i].time
        req_list.append([["Name", name], ["Blood Group", bg], ["Age", age], ["Date", date_rec], ["Time", time_rec]])
    
    context['req_list'] = req_list
    if requests.method == "POST":
        for i in range(len(req_list)):
            if requests.POST.get('checkbox' + str(i)) == "":
                Receiving.objects.filter(receiver_name=receivers[i].receiver_name, hosp_email=requests.session['email']).update(status = "Accepted")
            
        return redirect('receiver_requests')
        
    return render(requests, 'receiver_requests.html', context)

def accepted_rec_requests(requests):
    context = {}
    receivers = Receiving.objects.filter(status="Accepted", hosp_email=requests.session['email'])
    req_list = []
    for i in range(len(receivers)):
        name = receivers[i].receiver_name
        bg = Receiver.objects.filter(name=name)[0].bg
        dob = Receiver.objects.filter(name=name)[0].dob
        age = date.today().year - dob.year - ((date.today().month, date.today().day) < (dob.month, dob.day))
        date_rec = receivers[i].date
        time_rec = receivers[i].time
        req_list.append([["Name", name], ["Blood Group", bg], ["Age", age], ["Date", date_rec], ["Time", time_rec]])
    
    context['req_list'] = req_list
    if requests.method == "POST":
        for i in range(len(req_list)):
            if requests.POST.get('checkbox' + str(i)) == "":
                Receiving.objects.filter(receiver_name=receivers[i].receiver_name, hosp_email=requests.session['email']).update(status = "Received")
                if Receiver.objects.filter(name=receivers[i].receiver_name)[0].bg == "A+":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].Apos
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(Apos=quant-1)
                elif Receiver.objects.filter(name=receivers[i].receiver_name)[0].bg == "A-":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].Aneg
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(Aneg=quant-1)
                elif Receiver.objects.filter(name=receivers[i].receiver_name)[0].bg == "B+":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].Bpos
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(Bpos=quant-1)
                elif Receiver.objects.filter(name=receivers[i].receiver_name)[0].bg == "B-":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].Bneg
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(Bneg=quant-1)
                elif Receiver.objects.filter(name=receivers[i].receiver_name)[0].bg == "AB+":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].ABpos
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(ABpos=quant-1)
                elif Receiver.objects.filter(name=receivers[i].receiver_name)[0].bg == "AB-":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].ABneg
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(ABneg=quant-1)
                elif Receiver.objects.filter(name=receivers[i].receiver_name)[0].bg == "O+":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].Opos
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(Opos=quant-1)
                elif Receiver.objects.filter(name=receivers[i].receiver_name)[0].bg == "O-":
                    quant = Blood_group.objects.filter(hosp_email=requests.session['email'])[0].Oneg
                    Blood_group.objects.filter(hosp_email=requests.session['email']).update(Oneg=quant-1)
        return redirect('accepted_rec_requests')
    return render(requests, 'accepted_rec_requests.html', context)



def hosp_prev_records(requests):
    context = {}
    receivings = Receiving.objects.filter(hosp_email=requests.session['email'], status="Received")
    hosp_rec = []
    for i in range(len(receivings)):
        name = receivings[i].receiver_name
        bg = Receiver.objects.filter(name=name)[0].bg
        hosp_rec.append([name, bg])
    context['hosp_rec'] = hosp_rec
    context['length_rec'] = len(receivings)

    donations = Donation.objects.filter(hosp_email=requests.session['email'], status="Donated")
    hosp_don = []
    for i in range(len(donations)):
        name = donations[i].donor_name
        bg = Donor.objects.filter(name=name)[0].bg
        hosp_don.append([name, bg])
    context['hosp_don'] = hosp_don
    context['length_don'] = len(donations)
    return render(requests, 'hosp_prev_records.html', context)