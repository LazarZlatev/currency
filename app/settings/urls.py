
from django.contrib import admin
from django.urls import path
from currency.views import rate_list, contactus_list, status_code


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list', rate_list),
    path('contactus/list', contactus_list),
    path('sc/', status_code),
]
