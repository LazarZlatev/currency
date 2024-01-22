from django.urls import path
from currency.api.views import RateListAPIView, RateDetailAPIView

app_name = 'currency_api'

urlpatterns = [
    path('rates/', RateListAPIView.as_view(), name='rate-list'),
    path('rates/<int:pk>/', RateDetailAPIView.as_view(), name='rate-update'),
]
