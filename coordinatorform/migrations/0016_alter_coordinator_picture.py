# Generated by Django 4.2.3 on 2023-08-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinatorform', '0015_alter_coordinator_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinator',
            name='picture',
            field=models.ImageField(blank=True, default='coordinatorform/SBLOGO.png', null=True, upload_to='profilepics/'),
        ),
    ]
