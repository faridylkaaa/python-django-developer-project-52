from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class UserTest(TestCase):
    
    def setUp(self) -> None:
        self.user = User.objects.create(username='username', password='AdAp6911')
        self.user.save()
        self.id = self.user.id
        
    def test_update_user(self):
        self.user.username = 'new_username'
        self.user.save()
        self.assertEqual(self.user.username, 'new_username')
        
    def test_save_user(self):
        self.assertEqual(self.user, User.objects.get(id=self.id))
        
    def test_delete_user(self):
        self.user.delete()
        self.assertTrue(self.user not in User.objects.all())