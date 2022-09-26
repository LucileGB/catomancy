from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Account

class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')

class AccountChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'password')