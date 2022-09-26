from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AccountCreationForm, AccountChangeForm
from .models import Account

class AccountAdmin(UserAdmin):
    ordering = ('email', 'username', 'is_staff', 'is_superuser',)
    list_filter = ('email', 'username', 'is_staff', 'is_superuser',)
    list_display = ['email', 'username', 'is_staff', 'is_superuser', 'date_joined']
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username',
                                    'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )
    
    model = Account
    form = AccountChangeForm
    add_form = AccountCreationForm


admin.site.register(Account, AccountAdmin)