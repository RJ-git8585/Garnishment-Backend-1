# Generated by Django 4.2.1 on 2024-07-18 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_app', '0013_calculation_data_results'),
    ]

    operations = [
        migrations.CreateModel(
            name='application_activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_id', models.IntegerField()),
                ('employer_name', models.CharField(max_length=100)),
                ('action', models.CharField(max_length=255)),
                ('details', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
