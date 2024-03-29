import requests
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from currency.models import Rate, Source
from currency.choices import CurrencyTypeChoices, CurrencyTypeChoicesMono
from currency.constants import PRIVATBANK_CODE_NAME, MONOBANK_CODE_NAME
from currency.utils import to_2_places_decimal


@shared_task
def parse_monobank():
    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()

    source, _ = Source.objects.get_or_create(code_name=MONOBANK_CODE_NAME, defaults={'name': 'MonoBank'})

    available_currency_types = {
        '840': CurrencyTypeChoicesMono.USD,
        '980': CurrencyTypeChoicesMono.EUR
    }

    rates = response.json()
    for rate in rates:
        if 'rateBuy' not in rate:
            continue
        buy = to_2_places_decimal(rate['rateBuy'])
        sell = to_2_places_decimal(rate['rateSell'])
        currency_type_mono = rate['currencyCodeA']
        if str(currency_type_mono) not in available_currency_types:
            continue

        currency_type_mono = available_currency_types[str(currency_type_mono)]

        last_rate = Rate.objects.filter(source=source, currency_type_mono=currency_type_mono).order_by('created').last()

        if last_rate is None or (last_rate.buy != buy or last_rate.sell != sell):
            Rate.objects.create(
                buy=buy,
                sell=sell,
                currency_type_mono=currency_type_mono,
                source=source,
            )


@shared_task
def parse_privatbank():
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
    response = requests.get(url)
    response.raise_for_status()

    source, _ = Source.objects.get_or_create(code_name=PRIVATBANK_CODE_NAME, defaults={'name': 'PrivatBank'})

    available_currency_types = {
        'USD': CurrencyTypeChoices.USD,
        'EUR': CurrencyTypeChoices.EUR
    }

    rates = response.json()
    for rate in rates:
        buy = to_2_places_decimal(rate['buy'])
        sell = to_2_places_decimal(rate['sale'])
        currency_type = rate['ccy']

        if currency_type not in available_currency_types:
            continue

        currency_type = available_currency_types[currency_type]

        last_rate = Rate.objects.filter(source=source, currency_type=currency_type).order_by('created').last()

        if last_rate is None or (last_rate.buy != buy or last_rate.sell != sell):
            Rate.objects.create(
                buy=buy,
                sell=sell,
                currency_type=currency_type,
                source=source,
            )


@shared_task(autoretry_for=(ConnectionError,), retry_kwargs={
    'max_retries': 5
})
def send_email_in_background(subject, body):
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
    )
