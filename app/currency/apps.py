from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'

    def ready(self):
        import account.receivers # NOQA F401


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
