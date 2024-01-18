from django.db import models


class CurrencyTypeChoices(models.IntegerChoices):
    USD = 1, 'Dollar'
    EUR = 2, 'Euro'


class CurrencyTypeChoicesMono(models.IntegerChoices):
    USD = 840, 'Dollar'
    EUR = 980, 'Euro'
