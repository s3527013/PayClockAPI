from rest_framework import serializers

from .models import ClockEntry


class ClockEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClockEntry
        fields = ['id', 'user', 'clock_in_time', 'clock_out_time', 'duration', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
