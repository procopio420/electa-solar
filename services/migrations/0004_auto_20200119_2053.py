# Generated by Django 3.0.2 on 2020-01-19 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20200119_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icons/'),
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
