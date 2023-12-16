from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
