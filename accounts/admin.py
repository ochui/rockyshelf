from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email', 'phone_number']
    list_filter = ['date_joined', 'last_login', 'is_active', 'is_staff']
    search_fields = ['username', 'email', 'phone_number']
    fieldsets = UserAdmin.fieldsets + (
        ('KYC', {'fields': ('phone_number', 'gender', 'date_of_birth')}),
        ('Academic', {'fields': ('school', 'faculty', 'department')})
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('KYC', {'fields': ('phone_number', 'gender', 'date_of_birth')}),
        ('Academic', {'fields': ('school', 'faculty', 'department')})
    )
    
    model = CustomUser
