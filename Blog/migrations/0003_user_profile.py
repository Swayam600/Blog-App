# Generated by Django 3.1.1 on 2020-09-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Profile',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
