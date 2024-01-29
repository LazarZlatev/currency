from django.urls import reverse
from currency.models import Source


def test_get_source_list(api_client_auth):
    response = api_client_auth.get(reverse('source_api:source-list'))
    assert response.status_code == 200
    assert response.json()


def test_post_source_empty_body(api_client_auth):
    response = api_client_auth.post(reverse('source_api:source-list'))
    assert response.status_code == 400
    assert response.json() == {'name': ['This field is required.'],
                               'code_name': ['This field is required.']
                               }


def test_post_source_list_valid_data(api_client_auth):
    initial_count = Source.objects.count()
    payload = {'name': 'Test',
               'code_name': 'test'
               }

    response = api_client_auth.post(reverse('source_api:source-list'), data=payload)
    assert response.status_code == 201
    assert Source.objects.count() == initial_count + 1
