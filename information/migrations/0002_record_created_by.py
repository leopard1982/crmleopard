# Generated by Django 4.2.1 on 2023-05-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='created_by',
            field=models.CharField(default='', max_length=100),
        ),
    ]