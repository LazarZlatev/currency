from currency.api.views import RateViewSet
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'rates', RateViewSet, basename='rate')
app_name = 'currency_api'

urlpatterns = [
]+router.urls
