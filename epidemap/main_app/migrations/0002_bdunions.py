# Generated by Django 2.2 on 2020-03-20 19:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BdUnions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('div_id', models.CharField(max_length=254)),
                ('dist_id', models.CharField(max_length=254)),
                ('upz_id', models.CharField(max_length=254)),
                ('un_id', models.CharField(max_length=254)),
                ('un_uid', models.CharField(max_length=254)),
                ('divi_name', models.CharField(max_length=254)),
                ('dist_name', models.CharField(max_length=254)),
                ('upaz_name', models.CharField(max_length=254)),
                ('uni_name', models.CharField(max_length=254)),
                ('area_sqkm', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'BDUnions',
            },
        ),
    ]
