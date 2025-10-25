from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'user', 'title', 'posted_date', 'created_at', 'updated_at']
