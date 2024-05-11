from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
