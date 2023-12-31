from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.views.post import PostViewSet

router = DefaultRouter()
router.register('', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]
