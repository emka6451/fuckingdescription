# Generated by Django 2.2.2 on 2019-08-31 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_event_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]