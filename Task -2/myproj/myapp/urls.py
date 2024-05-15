from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductionLogViewSet  

router = DefaultRouter()
router.register(r'production_logs', ProductionLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
