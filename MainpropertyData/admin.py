from django.contrib import admin
from MainpropertyData.models import Mainproperty

class MainpropertyAdmin(admin.ModelAdmin):
    list_display = ('user_id','image','title','details','PostDate','WriterName')


admin.site.register(Mainproperty,MainpropertyAdmin)

# Register your models here.

