# Generated by Django 2.1.1 on 2018-10-26 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_emp_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='comment_count',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='book',
            name='poll_count',
            field=models.IntegerField(default=100),
        ),
    ]
