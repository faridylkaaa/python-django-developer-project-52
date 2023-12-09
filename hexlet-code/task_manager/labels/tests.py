from django.test import TestCase
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from django.contrib.auth.models import User
from task_manager.labels.models import Label

# Create your tests here.
class TaskTest(TestCase):
    
    def setUp(self) -> None:
        self.label = Label.objects.create(name='name')
        self.label.save()
        self.id = self.label.id
        
    def test_save_task(self):
        self.assertEqual(self.label.name, 'name')
        
    def test_update_task(self):
        self.label.name = 'new_name'
        self.label.save()
        self.assertEqual(self.label.name, 'new_name')
        
        
    def test_delete_task(self):
        '''найти тесты с except'''
        self.label.delete()
        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(name="name")
        # self.assertTrue(self.task not in Task.objects.all())