# Generated by Django 4.2.1 on 2023-07-21 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_hubapp', '0019_alter_application_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicants',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='applicants',
            name='resume',
        ),
    ]
