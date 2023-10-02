from django.contrib import admin
from .models import student, patient_record, hostel_record

# Register your models here.

admin.site.register(student)
admin.site.register(patient_record)
admin.site.register(hostel_record)