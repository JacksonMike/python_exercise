from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32)
    CHOICES = ((1, "Python"), (2, "Linux"), (3, "go"))
    category = models.IntegerField(choices=CHOICES)
    pub_time = models.DateField()
    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE)
    authors = models.ManyToManyField(to="Author")

    def __str__(self):
        return self.title


class Publisher(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
