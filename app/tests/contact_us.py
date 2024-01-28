from django.urls import reverse
from django.conf import settings
from currency.models import ContactUs


def test_post_contact_us_empty_form(client):
    response = client.post(reverse('currency:contactus-create'))
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'name': ['This field is required.'],
                                                    'email': ['This field is required.'],
                                                    'subject': ['This field is required.'],
                                                    'body': ['This field is required.']}


def test_post_contact_us_invalid_email(client):
    payload = {
        'name': 'name',
        'email': 'INVALID_EMAIL',
        'subject': 'subject',
        'body': 'body'
    }
    response = client.post(reverse('currency:contactus-create'), data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'email': ['Enter a valid email address.']}


def test_post_contact_us_valid_data(client, mailoutbox):
    initial_count = ContactUs.objects.count()
    payload = {
        'name': 'name',
        'email': 'lazarzlatev81@gmail.com',
        'subject': 'subject',
        'body': 'body'
    }
    response = client.post(reverse('currency:contactus-create'), data=payload)
    assert response.status_code == 302
    assert response.headers['Location'] == '/'
    assert len(mailoutbox) == 1
    assert mailoutbox[0].from_email == settings.DEFAULT_FROM_EMAIL
    assert ContactUs.objects.count() == initial_count + 1
