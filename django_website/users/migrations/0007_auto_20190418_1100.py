# Generated by Django 2.2 on 2019-04-18 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190418_1058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='messages',
            new_name='message',
        ),
    ]