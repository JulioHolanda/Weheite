# Generated by Django 4.1.1 on 2022-10-24 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_reply_likes_reply_liked_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='body',
            field=models.TextField(max_length=999),
        ),
    ]
