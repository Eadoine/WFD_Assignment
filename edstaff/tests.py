from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Applicant, Company, Job, Application
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your tests here.
class UserLoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_login(self):
        response = self.client.post(reverse('user_login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the User Homepage")
        self.assertTemplateUsed(response, 'edstaff/user_homepage.html')
        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertContains(response, "Logout")
        self.assertContains(response, "User Profile")
        self.assertContains(response, "Job Listings")
        self.assertContains(response, "Apply for Jobs")
        self.assertContains(response, "View Applications")
        self.assertContains(response, "Search Jobs")
