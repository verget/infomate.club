# Generated by Django 2.2.8 on 2020-01-19 18:20

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_auto_20200119_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardfeed',
            name='conditions',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
