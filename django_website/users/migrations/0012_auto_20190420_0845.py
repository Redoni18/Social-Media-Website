# Generated by Django 2.2 on 2019-04-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190419_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='public',
            field=models.BooleanField(default=False, verbose_name='Public '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='statusi',
            field=models.CharField(blank=True, choices=[('Engaget', 'Engaget'), ('In a relationship', 'In a relationship'), ('Married', 'Married'), ('Single', 'Single')], max_length=50, null=True),
        ),
    ]
