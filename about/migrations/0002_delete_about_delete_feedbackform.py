# Generated by Django 4.2.17 on 2025-01-15 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='FeedbackForm',
        ),
    ]
