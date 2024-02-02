from rest_framework import routers
from currency.api_source.views import SourceViewSet

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'sources', SourceViewSet, basename='source')

app_name = 'source_api'

urlpatterns = [
              ] + router.urls
