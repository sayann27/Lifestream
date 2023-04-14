from django.contrib import admin
from home.models import Receiver, Donor, Hospital, Donation, City

# Register your models here.
# admin.site.register(Registration)
admin.site.register(Receiver)
admin.site.register(Donor)
admin.site.register(Hospital)
admin.site.register(Donation)
admin.site.register(City)