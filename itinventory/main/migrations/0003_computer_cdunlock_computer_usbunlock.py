# Generated by Django 4.0.2 on 2022-03-11 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_loghistory_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='cdunlock',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='usbunlock',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
