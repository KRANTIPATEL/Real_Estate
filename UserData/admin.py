from django.contrib import admin
from UserData.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','password')


admin.site.register(User,UserAdmin)
# Register your models here.
