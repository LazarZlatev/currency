from unittest.mock import MagicMock
from currency.tasks import parse_privatbank
from currency.models import Rate
from currency.models import Source
from currency.constants import PRIVATBANK_CODE_NAME
from currency.choices import CurrencyTypeChoices


def test_parse_privatbank(mocker):
    initial_data = Rate.objects.count()

    privatbank_data = [
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "40.95000", "sale": "41.95000"},
        {"ccy": "USD", "base_ccy": "UAH", "buy": "37.60000", "sale": "38.20000"},
        {"ccy": "PLN", "base_ccy": "UAH", "buy": "37.60000", "sale": "38.20000"},
    ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: privatbank_data)
    )
    parse_privatbank()

    assert Rate.objects.count() == initial_data + 2
    assert requests_get_mock.call_count == 1
    assert requests_get_mock.call_args[0][0] == 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'


def test_privatbank_prevent_duplicates(mocker):
    privatbank_data = [
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "40.95000", "sale": "41.95000"},
        {"ccy": "USD", "base_ccy": "UAH", "buy": "37.60000", "sale": "38.20000"},
        {"ccy": "PLN", "base_ccy": "UAH", "buy": "37.60000", "sale": "38.20000"},
    ]

    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: privatbank_data)
    )

    source = Source.objects.get(code_name=PRIVATBANK_CODE_NAME)
    Rate.objects.create(source=source, buy="40.95000", sell="41.95000", currency_type=CurrencyTypeChoices.EUR)
    Rate.objects.create(source=source, buy="37.60000", sell="38.20000", currency_type=CurrencyTypeChoices.USD)
    initial_data = Rate.objects.count()
    parse_privatbank()

    assert Rate.objects.count() == initial_data
    assert requests_get_mock.call_count == 1
