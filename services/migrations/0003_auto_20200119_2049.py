# Generated by Django 3.0.2 on 2020-01-19 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20200119_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
    ]
