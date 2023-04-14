from django.db import models

# Create your models here.

# make city as a table


# class Registration(models.Model):
#     name = models.CharField(max_length=122)
#     email = models.CharField(max_length=122)
#     dob = models.DateField()
#     phone = models.CharField(max_length=13)
#     bg = models.CharField(max_length=3)
#     user_type = models.CharField(max_length=20)
#     addline1 = models.TextField()
#     addline2 = models.TextField()
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     pincode = models.IntegerField()
#     pwd = models.CharField(max_length=16)
    

class City(models.Model):
    name = models.CharField(max_length=122)

class Hospital(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=13)
    addline1 = models.TextField()
    addline2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    cover_image = models.TextField(null = True)  
    pwd = models.CharField(max_length=16)
    city_ID = models.ForeignKey("home.City", null=True, on_delete=models.SET_NULL)
    # put hospital id here which will link blood_group table
    

class Blood_group(models.Model):
    # make a field hospital id as foreign key 
    hosp_id = models.ForeignKey("home.Hospital", null=True, on_delete=models.SET_NULL)
    hosp_email = models.CharField(max_length=122, null=True, blank=True)
    Apos = models.IntegerField(default=0, blank=True)
    Aneg = models.IntegerField(default=0, blank=True)
    Bpos = models.IntegerField(default=0, blank=True)
    Bneg = models.IntegerField(default=0, blank=True)
    ABpos = models.IntegerField(default=0, blank=True)
    ABneg = models.IntegerField(default=0, blank=True)
    Opos = models.IntegerField(default=0, blank=True)
    Oneg = models.IntegerField(default=0, blank=True)

class Donation(models.Model):
    donor_name = models.CharField(max_length=122)
    hosp_name = models.CharField(max_length=122)
    hosp_email = models.CharField(max_length=122)
    time = models.TimeField()
    date = models.DateField(null=True)
    city = models.CharField(max_length=100)
    status = models.CharField(max_length=50, null=True, blank=True)
    city_ID = models.ForeignKey("home.City", null=True, on_delete=models.SET_NULL)

class Receiving(models.Model):
    receiver_name = models.CharField(max_length=122)
    hosp_name = models.CharField(max_length=122)
    hosp_email = models.CharField(max_length=122)
    time = models.TimeField()
    date = models.DateField(null=True)
    city = models.CharField(max_length=100)
    status = models.CharField(max_length=50, null=True, blank=True)
    city_ID = models.ForeignKey("home.City", null=True, on_delete=models.SET_NULL)


class Receiver(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    dob = models.DateField()
    phone = models.CharField(max_length=13)
    bg = models.CharField(max_length=3)
    addline1 = models.TextField()
    addline2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    medical_records = models.TextField(null = True, blank=True, default="None")
    pincode = models.IntegerField()
    pwd = models.CharField(max_length=16)
    city_ID = models.ForeignKey("home.City", null=True, on_delete=models.SET_NULL)


class Donor(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    dob = models.DateField()
    phone = models.CharField(max_length=13)
    bg = models.CharField(max_length=3)
    addline1 = models.TextField()
    addline2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    pwd = models.CharField(max_length=16)
    medical_records = models.TextField(null = True, blank=True, default="None")
    city_ID = models.ForeignKey("home.City", null=True, on_delete=models.SET_NULL)
