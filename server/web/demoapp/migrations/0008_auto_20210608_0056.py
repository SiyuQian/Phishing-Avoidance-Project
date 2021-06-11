# Generated by Django 3.2 on 2021-06-08 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0007_response_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='request_body',
        ),
        migrations.AddField(
            model_name='request',
            name='device',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='request',
            name='hr',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='request',
            name='ppg',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='request',
            name='time',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='request',
            name='timedate',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='request',
            name='uuid',
            field=models.CharField(default='', max_length=50),
        ),
    ]