# Generated by Django 2.2 on 2019-07-10 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogi', '0002_post_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='public',
        ),
    ]
