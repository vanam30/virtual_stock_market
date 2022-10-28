from django.contrib import admin

# Register your models here.
from .models import Person,Pending_Buy_Order

admin.site.register(Person)
admin.site.register(Pending_Buy_Order)