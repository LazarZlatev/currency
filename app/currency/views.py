from django.http.response import HttpResponse
from currency.models import ContactUs
from currency.models import Rate


def rate_list(request):
    results = []
    rates = Rate.objects.all()
    for rate in rates:
        results.append(
            f'ID: {rate.id}  buy: {rate.buy}, sell: {rate.sell}, type:{rate.type},'
            f' source: {rate.source}, created:{rate.created}'
        )
        return HttpResponse(str(results))


def contactus_list(request):
    results = []
    contactus = ContactUs.objects.all()
    for contact in contactus:
        results.append(
            f'ID: {contact.id}  buy: {contact.email_from}, sell: {contact.subject}, type:{contact.message}'
        )
        return HttpResponse(str(results))
