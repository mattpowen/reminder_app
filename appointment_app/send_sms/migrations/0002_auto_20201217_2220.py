# Generated by Django 3.1.4 on 2020-12-17 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_sms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='to_number',
            field=models.CharField(max_length=12),
        ),
    ]
