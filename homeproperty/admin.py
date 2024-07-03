from django.contrib import admin
from homeproperty.models import Home_Property

class HomepropertyAdmin(admin.ModelAdmin):
    list_display = ('time','img_link','status','Price','name','location','area','beds','bathroom')


admin.site.register(Home_Property,HomepropertyAdmin)
# Register your models here.
