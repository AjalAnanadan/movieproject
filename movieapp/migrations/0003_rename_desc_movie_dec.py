# Generated by Django 4.1.3 on 2022-12-20 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='desc',
            new_name='dec',
        ),
    ]
