from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User 
from django.contrib.auth.forms import  UserChangeForm
# Register your models here.

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class CustomUserAdmin(UserAdmin):
    model = User
    form = CustomUserChangeForm
    fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': [ 
                'email', 
                'username',
                'password', 
                'is_staff', 
            ]}
        ),
    ]
    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': [ 
                'username',
                'email',
                'password1', 
                'password2', 
            ]}
        ),
    ]
    search_fields = ['username', 'email']
    ordering = ['username']
    

admin.site.register(User, CustomUserAdmin)