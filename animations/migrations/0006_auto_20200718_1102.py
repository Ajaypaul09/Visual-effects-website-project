# Generated by Django 2.1.5 on 2020-07-18 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animations', '0005_auto_20200717_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=299)),
                ('number', models.BigIntegerField()),
                ('password', models.TextField()),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='contacts',
            name='number',
            field=models.BigIntegerField(),
        ),
    ]
