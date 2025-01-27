# Generated by Django 5.1.4 on 2025-01-23 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyCare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=255)),
                ('condition_description', models.TextField()),
                ('priority_level', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
