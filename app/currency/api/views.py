from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from currency.models import Rate

from currency.api.serializers import RateSerializer


class RateListAPIView(ListCreateAPIView):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer


class RateDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer
