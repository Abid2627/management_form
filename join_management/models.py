# Create your models here.
from django.db import models
class ManagementJoiningForm(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]


 

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    father_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    joining_date = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    aadhar_number = models.CharField(max_length=12)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
