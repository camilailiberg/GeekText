# Generated by Django 3.1.6 on 2021-02-23 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinelibrary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
    ]
