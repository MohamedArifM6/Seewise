from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Video, Profile
from .serializers import VideoSerializer, ProfileSerializer

class VideoProfileAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_video(self):
        video_data = {'name': 'Test Video', 'video_url': 'http://example.com/video.mp4', 'uploader': self.user.id}
        response = self.client.post('/api/videos/', video_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Video.objects.count(), 1)
        self.assertEqual(Video.objects.get().name, 'Test Video')

    def test_retrieve_video(self):
        video = Video.objects.create(name='Test Video', video_url='http://example.com/video.mp4', uploader=self.user)
        response = self.client.get(f'/api/videos/{video.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Video')

