# Generated by Django 2.1.5 on 2020-07-19 05:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('animations', '0007_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='address',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
