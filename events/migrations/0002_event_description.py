# Generated by Django 4.2.17 on 2025-01-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='Describe Event'),
        ),
    ]