# Generated by Django 4.1.2 on 2022-11-20 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_forum_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='professor',
        ),
        migrations.AddField(
            model_name='profile',
            name='professor',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]