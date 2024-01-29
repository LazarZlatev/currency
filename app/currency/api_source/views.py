from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from currency.models import Source
from currency.api_source.serializers import SourceSerializer


class SourceViewSet(ModelViewSet):
    queryset = Source.objects.all().order_by('name')
    serializer_class = SourceSerializer
    renderer_classes = (JSONRenderer, YAMLRenderer)
