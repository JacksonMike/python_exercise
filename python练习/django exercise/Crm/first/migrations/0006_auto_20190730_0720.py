# Generated by Django 2.2.3 on 2019-07-30 07:20

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_auto_20190728_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='course',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('JavaEE', 'python人工智能'), ('前端与移动开发', '软件测试')], max_length=14, null=True, verbose_name='咨询课程'),
        ),
    ]
