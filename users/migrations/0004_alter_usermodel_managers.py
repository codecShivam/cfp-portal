# Generated by Django 4.1.6 on 2023-04-22 07:02

from django.db import migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_usermodel_profile_delete_users'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usermodel',
            managers=[
                ('objects', users.models.CustomUserManager()),
            ],
        ),
    ]
