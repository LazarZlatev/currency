from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from account.models import User


@receiver(pre_save, sender=User)
def lower_user_email(instance, **kwargs):
    instance.email = instance.email.lower()


@receiver(post_save, sender=User)
def lower_user_email(sender, **kwargs):  # NOQA A811
    pass
