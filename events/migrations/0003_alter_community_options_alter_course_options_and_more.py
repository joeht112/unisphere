# Generated by Django 4.2.17 on 2025-01-16 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_event_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='community',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='community',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rating',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_tickets', to='events.event')),
                ('ticket_holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_tickets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
