# Generated by Django 4.2.1 on 2023-07-06 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_hubapp', '0014_alter_application_applicant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_hubapp.company'),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_hubapp.company'),
        ),
    ]