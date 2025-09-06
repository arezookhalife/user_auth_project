from django.test import TestCase
from accounts.models import User, UserPost, Comment

class UserModelTest(TestCase):
    def test_str(self):
        user = User.objects.create_user(username="tester", email="tester@example.com", password="12345")
        self.assertEqual(str(user), "tester")

class UserPostModelTest(TestCase):
    def test_str(self):
        user = User.objects.create_user(username="tester2", email="tester@example.com", password="12345")
        post = UserPost.objects.create(user=user, title="Test Post", content="Hello world")
        self.assertEqual(str(post), "Test Post")

class CommentModelTest(TestCase):
    def test_str(self):
        user = User.objects.create_user(username="tester3", email="tester@example.com", password="12345")
        post = UserPost.objects.create(user=user, title="Another Post", content="Testing...")
        comment = Comment.objects.create(user=user, post=post, content="Nice one!")
        self.assertIn("tester3", str(comment))
