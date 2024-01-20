import uuid
from django.templatetags.static import static
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


def user_directory_path(instance, filename):
    return f'avatars/user_{instance.id}/{filename}'


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.FileField(_('Avatar'), default=None, null=True, blank=True, upload_to=user_directory_path)
    phone_number = PhoneNumberField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    @property
    def avatar_url(self) -> str:
        if self.avatar:
            return self.avatar.url
        return static('download.png')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = uuid.uuid4()
        self.email = self.email.lower()

        instance = super().save(*args, **kwargs)

        return instance
