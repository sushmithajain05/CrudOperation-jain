# Generated by Django 5.0.6 on 2024-06-15 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('std', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='roll',
            field=models.IntegerField(unique=True),
        ),
    ]
