# Generated by Django 2.2.4 on 2020-02-05 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fm120k_db', '0011_auto_20200205_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seawatersample',
            name='collectionTiming',
        ),
        migrations.AddField(
            model_name='seawatersample',
            name='sampleDate',
            field=models.TextField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seawatersample',
            name='sampleTime',
            field=models.TextField(default=0, max_length=25),
            preserve_default=False,
        ),
    ]
