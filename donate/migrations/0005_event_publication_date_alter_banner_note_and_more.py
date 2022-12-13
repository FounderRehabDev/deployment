# Generated by Django 4.1.3 on 2022-11-06 04:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0004_alter_horse_note_alter_people_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('note', models.CharField(default='Image Dimensions 2000px X 2000px', editable=False, max_length=100)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Event Date')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(default="Don't forget to add a Description!", max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='note',
            field=models.CharField(default='Banner Image Dimensions: 2000px X 700px', editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='horse',
            name='note',
            field=models.CharField(default='Image Dimensions: 2000px By 2000px', editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='people',
            name='note',
            field=models.CharField(default='Image Dimensions: 2000px By 2000px', editable=False, max_length=100),
        ),
    ]
