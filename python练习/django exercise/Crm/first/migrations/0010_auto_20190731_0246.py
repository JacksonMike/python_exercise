# Generated by Django 2.2.3 on 2019-07-31 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0009_auto_20190731_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='class_list',
            field=models.ManyToManyField(blank=True, null=True, to='first.ClassList', verbose_name='已报班级'),
        ),
    ]
