from django_filters.rest_framework import FilterSet

from .models import ClockEntry


class ClockEntryFilter(FilterSet):
    class Meta:
        model = ClockEntry
        fields = {
            'clock_in_time': ['exact', 'gte', 'lte'],
            'clock_out_time': ['exact', 'gte', 'lte'],
        }
