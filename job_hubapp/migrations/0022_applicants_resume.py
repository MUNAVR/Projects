# Generated by Django 4.2.1 on 2023-07-22 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_hubapp', '0021_applicants_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicants',
            name='resume',
            field=models.FileField(default=None, upload_to='upload'),
        ),
    ]
