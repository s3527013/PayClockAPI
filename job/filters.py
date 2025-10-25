from django_filters.rest_framework import FilterSet

from .models import Job


class JobFilter(FilterSet):
    class Meta:
        model = Job
        fields = {
            'title': ['icontains'],
            'posted_date': ['exact', 'gte', 'lte'],
        }
