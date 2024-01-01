import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.FileField(_('Avatar'), default=None, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = uuid.uuid4()
            return super().save(*args, **kwargs)
