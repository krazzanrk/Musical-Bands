# Generated by Django 3.0.1 on 2020-01-07 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicalband',
            name='logo',
        ),
    ]
