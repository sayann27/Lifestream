from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("about", views.about, name = 'about'),
    path("venues", views.venues, name = 'venues'),
    path("login", views.login, name = 'login'),
    path("register", views.register, name = 'register'),
    path("receiver_login", views.receiver_login, name = 'receiver_login'),
    path("hospital_login", views.hospital_login, name = 'hospital_login'),
    path("donor_login", views.donor_login, name = 'donor_login'),    
    path("dashboard_donor", views.dashboard_donor, name = 'dashboard_donor'),
    path("logout", views.logout_view, name = 'logout'),
    path("donate", views.donate, name = 'donate'),
    path("my_donations", views.my_donations, name = 'my_donations'),
    path("medical_records", views.medical_records, name = 'medical_records'),
    path("hospital_list", views.hospital_list, name = 'hospital_list'),
    path("dashboard_receiver", views.dashboard_receiver, name = 'dashboard_receiver'),
    path("my_receivings", views.my_receivings, name = 'my_receivings'),
    path("receive", views.receive, name = 'receive'),
    path("dashboard_hospital", views.dashboard_hospital, name = 'dashboard_hospital'),
    path("hosp_blood", views.hosp_blood, name = 'hosp_blood'),
    path("hosp_info", views.hosp_info, name = 'hosp_info'),
    path("hosp_donors", views.hosp_donors, name = 'hosp_donors'),
    path("hosp_prev_records", views.hosp_prev_records, name = 'hosp_prev_records'),
    path("hosp_receivers", views.hosp_receivers, name = 'hosp_receivers'),
    path("donor_requests", views.donor_requests, name = 'donor_requests'),
    path("accepted_requests", views.accepted_requests, name = 'accepted_requests'),
    path("accepted_rec_requests", views.accepted_rec_requests, name = 'accepted_rec_requests'),
    path("receiver_requests", views.receiver_requests, name = 'receiver_requests'),
    

]
