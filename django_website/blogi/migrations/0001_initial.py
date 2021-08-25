# Generated by Django 2.2 on 2019-04-11 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulli', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title')),
                ('pershkrimi', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Content')),
                ('koha_posti', models.DateTimeField(default=django.utils.timezone.now)),
                ('foto', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='Fotot', verbose_name='Photo', width_field='width_field')),
                ('foto2', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='Fotot', verbose_name='Second Photo', width_field='width_field')),
                ('height_field', models.IntegerField(blank=True, default=0, null=True)),
                ('width_field', models.IntegerField(blank=True, default=0, null=True)),
                ('videofile', models.FileField(blank=True, null=True, upload_to='videos', verbose_name='Video')),
                ('autori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('koha_comment', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.TextField(blank=True, max_length=200, null=True)),
                ('photo', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='Fotot-comentet', width_field='width_field')),
                ('height_field', models.IntegerField(blank=True, default=0, null=True)),
                ('width_field', models.IntegerField(blank=True, default=0, null=True)),
                ('comment_autori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blogi.Post')),
            ],
            options={
                'ordering': ['-koha_comment'],
            },
        ),
    ]
