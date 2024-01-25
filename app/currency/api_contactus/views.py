from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from currency.models import ContactUs
from currency.api_contactus.serializers import ContactUsSerializer
from currency.api_contactus.paginators import ContactUsPagination
from currency.api_contactus.filters import ContactUsFilter
from rest_framework import filters


class ContactUsViewSet(ModelViewSet):
    queryset = ContactUs.objects.all().order_by('-name')
    serializer_class = ContactUsSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = ContactUsPagination
    filterset_class = ContactUsFilter
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email', 'created']
    ordering_fields = ('name', 'email', 'created')
