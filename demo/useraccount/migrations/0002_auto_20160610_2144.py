# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-10 21:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment_images',
            fields=[
                ('img_id', models.AutoField(primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Apartments',
            fields=[
                ('apat_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('rooms', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('roommates', models.IntegerField()),
                ('vacancy', models.IntegerField()),
                ('laundry', models.BooleanField()),
                ('internet', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default='images/img.JPG', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='has_apt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartment_images',
            name='apartment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccount.Apartments'),
        ),
    ]
