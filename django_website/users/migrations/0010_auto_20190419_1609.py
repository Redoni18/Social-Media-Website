# Generated by Django 2.2 on 2019-04-19 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190418_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='user',
            new_name='useri',
        ),
        migrations.AlterField(
            model_name='profile',
            name='statusi',
            field=models.CharField(blank=True, choices=[('In a relationship', 'In a relationship'), ('Single', 'Single'), ('Engaget', 'Engaget'), ('Married', 'Married')], max_length=50, null=True),
        ),
    ]
