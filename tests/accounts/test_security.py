from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User


class SecurityTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_csrf_enabled(self):
        response = self.client.get(reverse("accounts:login"))
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_sql_injection_protection(self):
        response = self.client.post(reverse("accounts:login"), {
            "username": "' OR 1=1 --",
            "password": "fakepass"
        })
        self.assertContains(response, "ورود")


class AccessControlTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='tester', email='tester@example.com', password='12345'
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('accounts:profile'))
        self.assertRedirects(
            response,
            f"{reverse('accounts:login')}?next={reverse('accounts:profile')}"
        )

    def test_access_when_logged_in(self):
        self.client.login(username='tester', password='12345')
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 200)


class XSSProtectionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='tester', email='tester@example.com', password='12345'
        )
        self.client.login(username='tester', password='12345')

    def test_post_content_escape(self):
        content = '<script>alert("XSS")</script>'
        response = self.client.post(
            reverse('accounts:create_post'),
            {'content': content}
        )
        self.assertNotIn(content, response.content.decode())


class SQLInjectionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='tester', email='tester@example.com', password='12345'
        )
        self.client.login(username='tester', password='12345')

    def test_search_safe(self):
        malicious_input = "' OR 1=1 --"
        response = self.client.post(
            reverse('accounts:search_posts'),
            {'query': malicious_input}
        )
        self.assertEqual(response.status_code, 200)