# Generated by Django 2.1.7 on 2019-03-16 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0005_auto_20190316_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignmentsubmissionform',
            old_name='assinmenttype',
            new_name='assinment_type',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmissionform',
            name='assignment_type',
        ),
    ]
