# Generated by Django 4.2.1 on 2023-07-21 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_hubapp', '0018_remove_job_applicant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(upload_to='upload'),
        ),
    ]
