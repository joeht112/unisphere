# Generated by Django 4.2.7 on 2025-01-16 15:29

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0006_alter_community_options_alter_community_description_and_more'),
        ('categories', '0002_remove_interests_author'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', django_summernote.fields.SummernoteTextField(blank=True)),
                ('profile_picture', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('communities', models.ManyToManyField(blank=True, to='events.community')),
                ('courses', models.ManyToManyField(blank=True, to='events.course')),
                ('events', models.ManyToManyField(blank=True, to='events.event')),
                ('interests', models.ManyToManyField(blank=True, to='categories.interests')),
                ('ratings', models.ManyToManyField(blank=True, to='events.rating')),
                ('tickets', models.ManyToManyField(blank=True, to='events.ticket')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]