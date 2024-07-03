from django.db import models
from datetime import date
from UserData.models import User

class Contactus(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    Firstname = models.CharField('First name', max_length=100)
    Lastname = models.CharField('last name', max_length=100)
    email = models.CharField('email', max_length=100)
    subject = models.CharField('subject', max_length=100)
    message = models.CharField('message', max_length=100)
# Create your models here.
