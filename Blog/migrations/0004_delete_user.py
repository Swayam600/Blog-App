# Generated by Django 3.1.1 on 2020-09-19 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_user_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
