# Generated by Django 4.2.3 on 2023-08-12 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinatorform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinator',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='coordinator',
            name='college',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='coordinator',
            name='contact',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='coordinator',
            name='dateofbirth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='coordinator',
            name='district',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='coordinator',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='coordinator',
            name='exp',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='coordinator',
            name='fullname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='coordinator',
            name='nickname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='coordinator',
            name='picture',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='coordinator',
            name='religion',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='coordinator',
            name='school',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='coordinator',
            name='upazila',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
