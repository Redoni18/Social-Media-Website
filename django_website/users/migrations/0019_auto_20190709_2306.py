# Generated by Django 2.2 on 2019-07-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20190709_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='public',
        ),
        migrations.AlterField(
            model_name='profile',
            name='statusi',
            field=models.CharField(blank=True, choices=[('Engaget', 'Engaget'), ('In a relationship', 'In a relationship'), ('Married', 'Married'), ('Single', 'Single')], max_length=50, null=True),
        ),
    ]