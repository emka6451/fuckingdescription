# Generated by Django 2.2.2 on 2019-08-31 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190831_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(blank=True, max_length=255),
        ),
    ]
