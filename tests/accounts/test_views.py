from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, UserPost

class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_status(self):
        response = self.client.get(reverse("accounts:home"))
        self.assertEqual(response.status_code, 200)

class ProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="profile_user", email="tester@example.com", password="12345")

    def test_profile_redirect_if_not_logged_in(self):
        response = self.client.get(reverse("accounts:profile"))
        self.assertRedirects(response, "/accounts/login/?next=/accounts/profile/")

    def test_profile_page_logged_in(self):
        self.client.login(username="profile_user", password="12345")
        response = self.client.get(reverse("accounts:profile"))
        self.assertEqual(response.status_code, 200)




