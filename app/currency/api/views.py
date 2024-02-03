from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from currency.models import Rate
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from currency.api.serializers import RateSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from currency.api.paginators import RatePagination
from currency.filters import RateFilter
from currency.api.throttling import RateThrottle
from currency.models import Source
from currency.choices import CurrencyTypeChoices
from app.currency.constants import LATEST_RATES_CACHE_KEY


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
    permission_classes = (AllowAny,)

    @action(methods=('GET',), detail=False, serializer_class=RateSerializer)
    def latest(self, request, *args, **kwargs):
        cached_data = cache.get(LATEST_RATES_CACHE_KEY)

        if cached_data is not None:
            return Response(cached_data)

        sources = Source.objects.all()
        latest_rates = []
        for source in sources:
            for currency in CurrencyTypeChoices:
                rate = Rate.objects.filter(source=source, currency_type=currency).order_by('-created').first()
                latest_rates.append(RateSerializer(instance=rate).data)

        cache.set(LATEST_RATES_CACHE_KEY, latest_rates, 60*60*24*7)

        return Response(latest_rates)
