# Generated by Django 2.2.4 on 2019-08-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fm120k_db', '0004_auto_20190829_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sewagesample',
            name='sampleStation',
            field=models.CharField(choices=[('18', '18'), ('A', 'A'), ('K6', 'K6'), ('Other', 'Other')], default=18, max_length=2),
        ),
    ]
