# Generated by Django 4.1.7 on 2023-04-01 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shrinkbot', '0009_remove_chat_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
