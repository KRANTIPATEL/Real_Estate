from django.db import models

class Home_Property(models.Model):
    
    time = models.CharField(max_length=25)
    img_link = models.ImageField(upload_to='img/media/images/')  # Path where images will be uploaded
    status = models.CharField(max_length=20)
    Price = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    area = models.CharField(max_length=50)
    beds = models.CharField(max_length=15)
    bathroom = models.CharField(max_length=15)
    
# Create your models here.
