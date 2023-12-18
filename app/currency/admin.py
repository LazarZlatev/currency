from django.contrib import admin
from rangefilter.filters import DateRangeFilterBuilder
from import_export.admin import ImportExportModelAdmin
from currency.models import Rate


@admin.register(Rate)
class RateAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'buy',
        'sell',
        'created',
        'currency_type',
        'source'
    )
    list_filter = (
        'currency_type',
        ('created', DateRangeFilterBuilder())
    )
    search_fields = (
        'buy',
        'sell',
        'source'
    )
    readonly_fields = (
        'buy',
        'sell'
    )
