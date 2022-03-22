# Generated by Django 3.2.5 on 2022-03-21 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=25)),
                ('open', models.CharField(max_length=25)),
                ('high', models.CharField(max_length=25)),
                ('low', models.CharField(max_length=25)),
                ('close', models.CharField(max_length=25)),
                ('adjclose', models.CharField(max_length=25)),
                ('volume', models.CharField(max_length=25)),
            ],
        ),
    ]
