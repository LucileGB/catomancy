from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _



class AccountManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


class Account(AbstractBaseUser, PermissionsMixin):
    """
    Handle user-specific logic (email, username, etc.)
    """
    objects = AccountManager()

    username = models.CharField(
        _("username"),
        max_length=100,
        unique=True,
        help_text=_("Required. 100 characters or fewer."),
        error_messages={
            "max_length": _("Please keep your username under 100 characters."),
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        _("email address"),
        max_length=260,
        unique=True,
        help_text=_("Required."),
        error_messages={
            "max_length": _("This email address is too long."),
            "unique": _("A user with that email address already exists."),
        },
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email.lower())