# Generated by Django 3.1.4 on 2021-01-07 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='email_message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
                ('to_address', models.EmailField(max_length=254)),
                ('reminder_date', models.DateField()),
                ('date_sent', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
