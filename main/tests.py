from django.test import TestCase
from .models import Group, Student

class ModelTestCase(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name='Group 1', description='Description of Group 1')
        self.student = Student.objects.create(name='John Doe', age=20, group=self.group)

    def test_group_creation(self):
        self.assertEqual(self.group.name, 'Group 1')
        self.assertEqual(self.group.description, 'Description of Group 1')

    def test_student_creation(self):
        self.assertEqual(self.student.name, 'John Doe')
        self.assertEqual(self.student.age, 20)
        self.assertEqual(self.student.group, self.group)
