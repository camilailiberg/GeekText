# Generated by Django 3.1.6 on 2021-04-04 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookdetails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingreview',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
