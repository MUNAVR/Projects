# Generated by Django 4.2.1 on 2023-06-26 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('company_name', models.CharField(max_length=100)),
                ('address', models.CharField(default='kochi', max_length=20)),
                ('type', models.CharField(default='it', max_length=20)),
                ('location', models.CharField(default='kochi', max_length=20)),
                ('logo', models.ImageField(default=None, upload_to='')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('salary', models.FloatField()),
                ('description', models.TextField(max_length=500)),
                ('experience', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=200)),
                ('skills', models.CharField(max_length=200)),
                ('vacancy', models.IntegerField()),
                ('qualification', models.CharField(max_length=50)),
                ('creation_date', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_hubapp.company')),
            ],
        ),
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='hh', max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('profile', models.ImageField(upload_to='')),
                ('resume', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
