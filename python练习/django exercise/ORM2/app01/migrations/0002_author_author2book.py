# Generated by Django 2.1.1 on 2018-10-25 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField(max_length=32)),
                ('email', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Author2Book',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Book')),
            ],
        ),
    ]
