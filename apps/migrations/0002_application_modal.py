# Generated by Django 3.0.2 on 2020-01-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='modal',
            field=models.CharField(default=7, max_length=150),
            preserve_default=False,
        ),
    ]
