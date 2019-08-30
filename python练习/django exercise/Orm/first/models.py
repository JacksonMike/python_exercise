from django.db import models


# Create your models here.
class Book(models.Model):
    """模型类插入数据"""
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish = models.ForeignKey(to="Publish", on_delete=models.CASCADE)  # 级联删除
    authors = models.ManyToManyField(to="Author")

    def __str__(self):
        return self.title


class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.CharField(max_length=32)
    ad = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    addr = models.CharField(max_length=32)
    tel = models.IntegerField()

    def __str__(self):
        return self.addr


class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    dep = models.CharField(max_length=32)
    pro = models.CharField(max_length=32)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
