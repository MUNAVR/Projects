# Generated by Django 4.2.1 on 2023-06-29 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_hubapp', '0003_alter_job_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.FloatField(max_length=6),
        ),
    ]
