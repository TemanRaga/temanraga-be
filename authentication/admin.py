from django.contrib import admin
from authentication.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_verified', 'gender', 'auth_provider']

admin.site.register(User, UserAdmin)