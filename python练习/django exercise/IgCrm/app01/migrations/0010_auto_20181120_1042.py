# Generated by Django 2.1.1 on 2018-11-20 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_auto_20181120_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classstudyrecord',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='讲师'),
        ),
        migrations.AlterField(
            model_name='student',
            name='class_list',
            field=models.ManyToManyField(blank=True, related_name='students', to='app01.ClassList', verbose_name='已报班级'),
        ),
        migrations.AlterUniqueTogether(
            name='studentstudyrecord',
            unique_together={('student', 'classstudyrecord')},
        ),
    ]
