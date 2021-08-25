# Generated by Django 2.2 on 2019-07-10 06:21

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20190709_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, default=django.contrib.auth.models.User, related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='statusi',
            field=models.CharField(blank=True, choices=[('In a relationship', 'In a relationship'), ('Engaget', 'Engaget'), ('Married', 'Married'), ('Single', 'Single')], max_length=50, null=True),
        ),
    ]