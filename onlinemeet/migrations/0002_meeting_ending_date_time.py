# Generated by Django 4.0.6 on 2022-08-07 06:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('onlinemeet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='ending_date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 7, 6, 53, 24, 974553, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
