from django.urls import path, include
from .views import VideoListCreateAPIView, VideoRetrieveUpdateDestroyAPIView, ProfileRetrieveAPIView

urlpatterns = [
    path('api/videos/', VideoListCreateAPIView.as_view(), name='video-list-create'),
    path('api/videos/<int:pk>/', VideoRetrieveUpdateDestroyAPIView.as_view(), name='video-retrieve-update-destroy'),
    path('api/profile/<str:user__username>/', ProfileRetrieveAPIView.as_view(), name='profile-retrieve'),
    path('api-auth/', include('rest_framework.urls')),
]