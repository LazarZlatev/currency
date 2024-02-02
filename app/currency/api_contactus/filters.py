import django_filters
from currency.models import ContactUs


class ContactUsFilter(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = {
            'name': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'email': ['exact', 'gt', 'gte', 'lt', 'lte'],
        }
