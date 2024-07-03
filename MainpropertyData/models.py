from django.db import models
from datetime import date
from UserData.models import User

class Mainproperty(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to='img/media/images/')  # Path where images will be uploaded
    # image1 = models.CharField(max_length=100)
    # image2 = models.CharField(max_length=100)
    title=models.CharField('Post Title',max_length=100)
    details=models.CharField('Post Details',max_length=1000)
    PostDate=models.DateField(default=date.today)
    WriterName=models.CharField('Write Name',max_length=100)

# Create your models here.
