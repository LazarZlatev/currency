from django_filters.rest_framework import DjangoFilterBackend
from currency.models import Rate
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from currency.api.serializers import RateSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from currency.api.paginators import RatePagination
from currency.filters import RateFilter
from currency.api.throttling import RateThrottle


class RateViewSet(ModelViewSet):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer
    renderer_classes = (JSONRenderer, YAMLRenderer)
    pagination_class = RatePagination
    filterset_class = RateFilter
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter
    )
    ordering_fields = ('buy', 'sell', 'created')
    throttle_classes = (RateThrottle,)
