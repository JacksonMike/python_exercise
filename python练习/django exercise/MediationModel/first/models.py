from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=32)
    courses = models.ManyToManyField("Course", through="Score")


class Course(models.Model):
    name = models.CharField(max_length=32)


class Score(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    score = models.IntegerField()
    