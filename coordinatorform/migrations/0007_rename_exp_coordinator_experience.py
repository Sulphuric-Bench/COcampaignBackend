# Generated by Django 4.2.3 on 2023-08-13 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coordinatorform', '0006_rename_user_coordinator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coordinator',
            old_name='exp',
            new_name='experience',
        ),
    ]