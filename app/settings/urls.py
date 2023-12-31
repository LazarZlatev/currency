from django.contrib import admin
from django.urls import path, include
from currency.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('account.urls')),
    path('currency/', include('currency.urls')),
    path('_debug__/', include('debug_toolbar.urls')),
    path('', IndexView.as_view(), name='index'),
]
