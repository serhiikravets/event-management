from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpass', first_name='Test', last_name='User')

    def test_create_user(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.email, 'testuser@gmail.com')
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertFalse(self.user.is_staff)
        self.assertTrue(self.user.is_active)

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser@gmail.com')

    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), 'Test User')

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(email='superuser@gmail.com', password='testpass')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
