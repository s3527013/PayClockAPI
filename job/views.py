from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .filters import JobFilter
from .models import Job
from .serializer import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = JobFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Job.objects.all()
        return Job.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
