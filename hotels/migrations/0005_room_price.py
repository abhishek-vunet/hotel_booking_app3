# Generated by Django 5.0.7 on 2024-08-01 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_alter_amenities_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
