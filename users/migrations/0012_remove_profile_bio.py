# Generated by Django 4.1.2 on 2022-11-21 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_forum_professor_profile_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]
