# Generated by Django 5.2.1 on 2025-05-17 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_customuser_last_names_customuser_names'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='last_names',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='names',
        ),
    ]
