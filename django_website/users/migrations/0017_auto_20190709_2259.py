# Generated by Django 2.2 on 2019-07-10 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20190421_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='statusi',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('In a relationship', 'In a relationship'), ('Married', 'Married'), ('Engaget', 'Engaget')], max_length=50, null=True),
        ),
    ]
