# Generated by Django 4.0.2 on 2022-02-25 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='help',
            name='address',
            field=models.CharField(default='Moldova', max_length=1000),
        ),
        migrations.AddField(
            model_name='needhelp',
            name='address',
            field=models.CharField(default='Moldova', max_length=1000),
        ),
    ]
