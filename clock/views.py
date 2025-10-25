from rest_framework import viewsets

from .filters import ClockEntryFilter
from .models import ClockEntry
from .serializers import ClockEntrySerializer


class ClockEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clock entries to be viewed or edited.
    """
    queryset = ClockEntry.objects.all()
    serializer_class = ClockEntrySerializer
    filterset_class = ClockEntryFilter

    def get_queryset(self):
        return ClockEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
