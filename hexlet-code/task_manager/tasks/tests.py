from django.test import TestCase
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from django.contrib.auth.models import User
from task_manager.tasks.filter import TaskFilter
from django.test import RequestFactory
from django.urls import reverse_lazy

# Create your tests here.
class TaskTest(TestCase):
    
    def setUp(self) -> None:
        self.author = User.objects.create(username='username', password='123456')
        self.status = Status.objects.create(name='status')
        self.task = Task.objects.create(name='name', status=self.status, author=self.author)
        self.task.save()
        self.id = self.task.id
        self.author2 = User.objects.create(username='username2', password='123456')
        self.status2 = Status.objects.create(name='status2')
        self.task_2 = Task.objects.create(name='name2', status=self.status2, author=self.author2)
        self.task_2.save()
        
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
        
    def test_filter(self):
        filter_data = {'status': self.status2.id, 'executor': '', 'labels': ''}
        factory = RequestFactory()
        request = factory.get(reverse_lazy('tasks:index'), filter_data)
        q = TaskFilter(request.GET, request=request, queryset=Task.objects.all())
        assert len(q.qs) == 1
        assert q.qs[0].status.name == 'status2'