# Generated by Django 2.1.7 on 2019-03-16 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0002_assignmentsubmissionform_accounts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentsubmissionform',
            name='admission_number',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmissionform',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmissionform',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmissionform',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmissionform',
            name='university',
        ),
    ]
