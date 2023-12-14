from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUp(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@test,com", password="test"
        )
        cls.post = Post.objects.create(
            auther=cls.user, title="a good title", body="a good body content"
        )

    def test_post_model(self):
        self.assertEqual(self.post.auther.username, "testuser")
        self.assertEqual(self.post.title, "a good title")
        self.assertEqual(self.post.body, "a good body content")
        self.assertEqual(str(self.post), "a good title")
