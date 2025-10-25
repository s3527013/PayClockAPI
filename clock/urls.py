from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClockEntryViewSet

router = DefaultRouter()
router.register(r'', ClockEntryViewSet, basename='clockentry')

urlpatterns = [
    path('', include(router.urls)),
]
