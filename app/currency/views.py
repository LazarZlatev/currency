from django.http.response import HttpResponse
from django.shortcuts import render
from currency.models import ContactUs
from currency.models import Rate


def rate_list(request):
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }
    return render(request, 'rate_list.html', context)


def contactus_list(request):
    contactus = ContactUs.objects.all()
    context = {
        'contactus': contactus
    }
    return render(request, 'contact_us.html', context)


def status_code(request):
    return HttpResponse('Redirect!',
                        status=301,
                        headers={'Location': '/rate/list'})
