from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.


class CustomUser(AbstractUser, PermissionsMixin):
    class AccountType(models.TextChoices):
        VIP = "V", _("VIP")
        FREE = "F", _("Free")

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    acc_type = models.CharField(choices=AccountType.choices, max_length=1, default="F")
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    profile_pic = models.ImageField(upload_to="user", blank=True, null=True)
    bio = models.TextField()
    date_joined = models.DateTimeField(default=timezone.now, editable=False, blank=True)

    def __str__(self) -> str:
        return self.username