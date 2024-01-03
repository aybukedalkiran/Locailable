from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from users.models import Profile

class ProfileModelTests(TestCase):

    def test_create_profile(self):
        user = User.objects.create_user(
            username="test_user",
            email="test@example.com",
            password="test_password",
        )
        profile = Profile.objects.create(
            user=user,
            name="Test User",
            email="test@example.com",
            username="test_username",
            bio="Test Bio",
        )

        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(profile.user.username, "test_user")
        self.assertEqual(profile.name, "Test User")
        self.assertEqual(profile.email, "test@example.com")
        self.assertEqual(profile.username, "test_username")
        self.assertEqual(profile.bio, "Test Bio")

    def test_profile_image_url(self):
        user = User.objects.create_user(
            username="test_user",
            email="test@example.com",
            password="test_password",
        )
        profile = Profile.objects.create(
            user=user,
            name="Test User",
            email="test@example.com",
            username="test_username",
            bio="Test Bio",
            profile_image="profiles/test_image.png",
        )

        self.assertEqual(profile.imageURL, "/media/profiles/test_image.png")

    def test_str_method(self):
        user = User.objects.create_user(
            username="test_user",
            email="test@example.com",
            password="test_password",
        )
        profile = Profile.objects.create(
            user=user,
            name="Test User",
            email="test@example.com",
            username="test_username",
            bio="Test Bio",
        )

        self.assertEqual(str(profile), "test_username")

    def test_username_field(self):
        self.assertEqual(Profile.USERNAME_FIELD, "username")
