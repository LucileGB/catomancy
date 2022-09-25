from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import PlayerCreationForm, PlayerChangeForm
from .models import Player, PlayerAccount

class PlayerAdmin(UserAdmin):
    # add_form = PlayerCreationForm
    # form = PlayerChangeForm
    model = Player
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


admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerAccount)