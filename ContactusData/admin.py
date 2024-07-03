from django.contrib import admin
from ContactusData.models import Contactus

class ContactusAdmin(admin.ModelAdmin):
    list_display = ('user_id','Firstname','Lastname','email','subject','message')


admin.site.register(Contactus,ContactusAdmin)

# Register your models here.

