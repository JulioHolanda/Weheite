# Generated by Django 4.1.2 on 2022-10-23 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_topic_forum_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
