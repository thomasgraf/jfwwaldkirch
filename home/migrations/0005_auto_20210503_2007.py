# Generated by Django 3.1.8 on 2021-05-03 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_webpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='date',
        ),
        migrations.RemoveField(
            model_name='webpage',
            name='intro',
        ),
    ]
