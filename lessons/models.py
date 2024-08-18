from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    max_students = models.PositiveIntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    lessons = models.ManyToManyField(Lesson, related_name='students')

    def __str__(self):
        return self.name
