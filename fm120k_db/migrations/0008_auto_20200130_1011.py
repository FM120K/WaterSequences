# Generated by Django 2.2.4 on 2020-01-30 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fm120k_db', '0007_auto_20191201_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seawatersample',
            name='sampleProcessed',
        ),
        migrations.AddField(
            model_name='seawatersample',
            name='Carb_Concentration',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seawatersample',
            name='Concentration',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seawatersample',
            name='DNA_Concentration',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seawatersample',
            name='F_readfile',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='seawatersample',
            name='R_readfile',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='seawatersample',
            name='TotalYield',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seawatersample',
            name='elutionVolume',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seawatersample',
            name='processed',
            field=models.CharField(choices=[('Processed', 'Processed'), ('Sent for Analysis', 'Sent for Analysis'), ('Analysis received', 'Analysis received')], default='Processed', max_length=20),
        ),
    ]
