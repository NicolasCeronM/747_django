# Generated by Django 5.2.1 on 2025-05-18 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designer', '0004_designerprofile_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designerprofile',
            name='full_name',
        ),
    ]
