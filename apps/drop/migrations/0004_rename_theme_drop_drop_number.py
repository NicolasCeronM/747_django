# Generated by Django 5.2.1 on 2025-05-16 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drop', '0003_alter_drop_options_alter_drop_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drop',
            old_name='theme',
            new_name='drop_number',
        ),
    ]
