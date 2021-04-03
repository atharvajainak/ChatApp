# Generated by Django 3.1.7 on 2021-04-03 14:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(code='Invalid Username', message='Username must be alphanumeric, may contain - or _', regex='^[a-zA-Z0-9_-]{3,50}$')])),
                ('position', models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student')], max_length=20)),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_creater', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
