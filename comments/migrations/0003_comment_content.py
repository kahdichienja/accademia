# Generated by Django 2.1.7 on 2019-03-17 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20190317_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
