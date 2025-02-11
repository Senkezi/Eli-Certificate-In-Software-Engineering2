# Generated by Django 4.2.4 on 2023-09-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('country', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=255)),
                ('zipcode', models.IntegerField(default=0)),
                ('phone1', models.CharField(max_length=15)),
                ('phone2', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
