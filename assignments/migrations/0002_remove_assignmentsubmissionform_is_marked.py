# Generated by Django 2.1.7 on 2019-03-17 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentsubmissionform',
            name='is_marked',
        ),
    ]
