from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, UserPost

class IntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="int_user", email="tester@example.com", password="12345")

    def test_create_post_flow(self):
        self.client.login(username="int_user", password="12345")
        response = self.client.post(reverse("accounts:create_post"), {
            "title": "Integration Post",
            "content": "Testing integration"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(UserPost.objects.filter(title="Integration Post").exists())