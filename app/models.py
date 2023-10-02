from django.db import models
from django.contrib.auth.models import User

# Create your models here.

genders = [
           ("Male","Male"),
           ("Female","Female"),
           ]

h_locations = [
           ("Obanla","Obanla"),
           ("Obakekere","Obakekere"),
           ("West-gate", "West-gate"),
           ]

levels = [
           ("100","100"),
           ("200","200"),
           ("300", "300"),
           ("400","400"),
           ("500","500"),
        ]
           
           

class student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    surname = models.CharField(null= False, max_length= 100)
    first_name = models.CharField(null= False, max_length= 100)
    last_name = models.CharField(null= True, max_length= 100)
    level = models.CharField(null= False, choices=levels, max_length= 4)
    gender = models.CharField(null= False, choices=genders, max_length= 100)
    department = models.CharField(null= False, max_length= 100)

    @classmethod
    def create(cls, request, **kwargs):
        username = request.user.username
        user = User.objects.get(username=username)
        instance = cls(user=user, **kwargs)
        instance.save()
        return instance
   


class patient_record(models.Model):
    student = models.OneToOneField(student, on_delete=models.CASCADE, null=True, blank=True)
    age = models.CharField(null= False, max_length= 100)
    ailment = models.CharField(null= False, max_length= 100)
    residence = models.CharField(null= False, max_length= 100)
    next_of_kin = models.CharField(null= False, max_length= 100)
    Relation_with_NOK = models.CharField(null= False, max_length= 100)
    nok_contact = models.CharField(null= False, max_length= 100)


class hostel_record(models.Model):
    student = models.OneToOneField(student, on_delete=models.CASCADE, null=True, blank=True)
    hostel_name = models.CharField(null= False, max_length= 100)
    location = models.CharField(null= False, choices=h_locations, max_length= 20)
    No_of_roommates = models.IntegerField(null= True)
    block_and_room_number = models.CharField(null= False, max_length= 100)