from django.core.validators import MaxValueValidator
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Cat(models.Model):
    name = models.CharField(
        max_length=100,
        error_messages={
            "max_length": _("Please keep your cat's name under 100 characters."),
        }
        )
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    affection = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(25)]
        )
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    follower = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following'
        )
    followee = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by'
        )

    class Meta:
        unique_together = ('follower', 'followee')