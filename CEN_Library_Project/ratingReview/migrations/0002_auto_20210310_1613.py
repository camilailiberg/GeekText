# Generated by Django 3.1.7 on 2021-03-10 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookdetails', '0001_initial'),
        ('ratingReview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrating',
            name='book',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='bookdetails.book'),
        ),
    ]