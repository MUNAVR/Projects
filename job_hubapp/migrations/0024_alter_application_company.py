# Generated by Django 4.2.1 on 2023-07-25 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_hubapp', '0023_alter_application_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_hubapp.company'),
        ),
    ]
