# Generated by Django 4.2.8 on 2023-12-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('Household_Name', models.CharField(max_length=255)),
                ('Area', models.CharField(max_length=255)),
                ('Creat_day', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
