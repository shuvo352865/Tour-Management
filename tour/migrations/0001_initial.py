# Generated by Django 4.1.7 on 2023-03-22 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='calculate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frm', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('transport', models.CharField(max_length=100)),
                ('hotel', models.CharField(max_length=100)),
                ('person', models.FloatField()),
                ('day', models.FloatField()),
            ],
        ),
    ]
