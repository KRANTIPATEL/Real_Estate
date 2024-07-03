from django.contrib import admin
from ServiceData.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('user_id','FullName','email','City','ApartmentSize','message')


admin.site.register(Service,ServiceAdmin)

# Register your models here.
