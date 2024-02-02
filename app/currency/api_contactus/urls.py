from rest_framework import routers
from currency.api_contactus.views import ContactUsViewSet

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'contacts', ContactUsViewSet, basename='contact_us')

app_name = 'contactus_api'

urlpatterns = [
]+router.urls
