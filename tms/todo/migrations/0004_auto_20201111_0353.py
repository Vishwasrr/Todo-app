# Generated by Django 3.1.2 on 2020-11-11 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_task_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='task',
        ),
    ]
