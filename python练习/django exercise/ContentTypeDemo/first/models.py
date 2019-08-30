from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db import models


# Create your models here.
class Meat(models.Model):
    name = models.CharField(max_length=32)
    # 用于反向查询
    coupons = GenericRelation(to="Coupon")


class Fruit(models.Model):
    name = models.CharField(max_length=32)
    coupons = GenericRelation(to="Coupon")


class Coupon(models.Model):
    title = models.CharField(max_length=32)
    # 定位到表
    content_type = models.ForeignKey(to=ContentType, on_delete=models.CASCADE)
    # 定位到对象
    object_id = models.IntegerField()
    # 用于关联的对象
    content_object = GenericForeignKey("content_type", "object_id")