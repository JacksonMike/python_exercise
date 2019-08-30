from django.db import models


# Create your models here.
class BookInfo(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
