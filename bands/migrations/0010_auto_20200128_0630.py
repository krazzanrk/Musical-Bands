# Generated by Django 3.0.1 on 2020-01-28 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0009_auto_20200109_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=None),
            preserve_default=False,
        ),
    ]