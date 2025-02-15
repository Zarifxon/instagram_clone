from django.contrib import admin

from users.models import User, UserConfirmation

# from models import ORDINARY_USER
# Register your models here.


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone_number']

admin.site.register(User, UserModelAdmin)
admin.site.register(UserConfirmation)
