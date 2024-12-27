# Generated by Django 5.1.4 on 2024-12-25 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_movie_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='featured_in',
            field=models.ManyToManyField(related_name='cast', to='movies.movie'),
        ),
    ]