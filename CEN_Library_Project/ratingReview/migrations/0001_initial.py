# Generated by Django 3.1.7 on 2021-03-09 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookdetails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default=1, max_length=128)),
                ('name', models.CharField(default='Write Review', max_length=128)),
                ('username', models.CharField(default='', max_length=128)),
                ('book', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='bookdetails.book')),
            ],
            options={
                'db_table': 'ratingReview_bookrating',
                'managed': True,
            },
        ),
    ]
