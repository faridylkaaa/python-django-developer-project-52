from django.test import TestCase
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from django.contrib.auth.models import User

# Create your tests here.
class TaskTest(TestCase):
    
    def setUp(self) -> None:
        self.author = User.objects.create(username='username', password='123456')
        self.status = Status.objects.create(name='status')
        self.task = Task.objects.create(name='name', status=self.status, author=self.author)
        self.task.save()
        self.id = self.task.id
        
    def test_save_task(self):
        self.assertEqual(self.task.name, 'name')
        self.assertEqual(self.task.author, self.author)
        self.assertEqual(self.task.status, self.status)
        
    def test_update_task(self):
        self.task.name = 'new_name'
        self.task.save()
        self.assertEqual(self.task.name, 'new_name')
        
        
    def test_delete_task(self):
        '''найти тесты с except'''
        self.task.delete()
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(name="name")
        # self.assertTrue(self.task not in Task.objects.all())