from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.
class TestViews(TestCase):

    def test_get_profile(self):
        user = User.objects.create(username='testuser')
        user.set_password('testuser123')
        user.save()
        self.client.login(username='testuser', password='testuser123')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
