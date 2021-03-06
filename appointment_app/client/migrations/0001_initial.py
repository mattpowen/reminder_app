# Generated by Django 3.1.4 on 2020-12-10 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('house_number', models.IntegerField()),
                ('house_name', models.CharField(max_length=255)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('address3', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=10)),
                ('telephone_number', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=10)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
    ]
