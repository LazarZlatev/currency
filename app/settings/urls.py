
from django.contrib import admin
from django.urls import path
from currency.views import rate_list
from currency.views import contactus_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list',rate_list),
    path('contactus/list',contactus_list),
]
