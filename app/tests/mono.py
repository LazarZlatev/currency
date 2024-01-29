from unittest.mock import MagicMock
from currency.constants import MONOBANK_CODE_NAME
from currency.choices import CurrencyTypeChoicesMono
from currency.tasks import parse_monobank
from currency.models import Rate
from currency.models import Source


def test_parse_monobank(mocker):
    initial_data = Rate.objects.count()

    monobank_data = [
        {"currencyCodeA": 840, "currencyCodeB": 980, "date": 1706523006, "rateBuy": 37.75, "rateSell": 38.1607},
        {"currencyCodeA": 978, "currencyCodeB": 980, "date": 1706523006, "rateBuy": 40.85, "rateSell": 41.5007},
        {"currencyCodeA": 978, "currencyCodeB": 840, "date": 1706479273, "rateBuy": 1.08, "rateSell": 1.09}
    ]

    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: monobank_data)
    )
    parse_monobank()

    assert Rate.objects.count() == initial_data + 1
    assert requests_get_mock.call_count == 1
    assert requests_get_mock.call_args[0][0] == 'https://api.monobank.ua/bank/currency'


def test_monobank_prevent_duplicates(mocker):
    monobank_data = [
        {"currencyCodeA": 840, "currencyCodeB": 980, "date": 1706523006, "rateBuy": 37.75, "rateSell": 38.1607},
        {"currencyCodeA": 978, "currencyCodeB": 980, "date": 1706523006, "rateBuy": 40.85, "rateSell": 41.5007},
        {"currencyCodeA": 978, "currencyCodeB": 840, "date": 1706479273, "rateBuy": 1.08, "rateSell": 1.09}
    ]

    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: monobank_data)
    )

    source = Source.objects.get(code_name=MONOBANK_CODE_NAME)
    Rate.objects.create(source=source,
                        buy="40.85",
                        sell="41.5007",
                        currency_type=CurrencyTypeChoicesMono.EUR)
    Rate.objects.create(source=source,
                        buy="37.75",
                        sell="38.1607",
                        currency_type=CurrencyTypeChoicesMono.USD)
    initial_data = Rate.objects.count()
    parse_monobank()

    assert Rate.objects.count() == initial_data
    assert requests_get_mock.call_count == 1
