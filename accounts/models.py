from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):

    GENDERCHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    
    gender = models.CharField(max_length=6, choices=GENDERCHOICES, null=True, blank=True)
    date_of_birth = models.DateField("date of birth", blank=True, null=True)
    phone_number = PhoneNumberField(verbose_name = "phone number", null=True, blank=True)
    school = models.CharField(max_length=200, blank=True)
    faculty = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    

    def get_absolute_url(self):
        return reverse("user_profile", args=[self.username])