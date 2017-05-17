# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cthd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mahoadon', models.IntegerField(blank=True, null=True)),
                ('thanhtien', models.IntegerField(blank=True, null=True)),
                ('masp', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cthd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sanpham',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masp', models.IntegerField(blank=True, null=True)),
                ('tensp', models.TextField()),
                ('gia', models.IntegerField(blank=True, null=True)),
                ('urlhinh', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sanpham',
                'managed': False,
            },
        ),
    ]
