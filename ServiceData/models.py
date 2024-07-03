from django.db import models
from datetime import date
from UserData.models import User

class Service(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    FullName = models.CharField('FullName', max_length=100)
    email = models.CharField('email', max_length=100)
    City = models.CharField('City', max_length=100)
    ApartmentSize = models.CharField('ApartmentSize', max_length=100)
    message = models.CharField('message', max_length=100)
# Create your models here.
