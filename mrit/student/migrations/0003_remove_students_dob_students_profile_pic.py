# Generated by Django 5.1.6 on 2025-02-21 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_rename_student_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='dob',
        ),
        migrations.AddField(
            model_name='students',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
