from django.test import TestCase
from task_manager.statuses.models import Status

# Create your tests here.
class UserTest(TestCase):
    
    def setUp(self) -> None:
        self.status = Status.objects.create(name='status')
        self.status.save()
        self.id = self.status.id
        
    def test_update_user(self):
        self.status.username = 'new_status'
        self.status.save()
        self.assertEqual(self.status.username, 'new_status')
        
    def test_save_user(self):
        self.assertEqual(self.status, Status.objects.get(id=self.id))
        
    def test_delete_user(self):
        self.status.delete()
        self.assertTrue(self.status not in Status.objects.all())