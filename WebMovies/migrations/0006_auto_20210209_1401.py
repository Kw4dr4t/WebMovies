# Generated by Django 3.1.6 on 2021-02-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebMovies', '0005_auto_20210209_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(8, 'Historical'), (4, 'Crime'), (7, 'Fantasy'), (3, 'Comedy'), (13, 'Wester'), (11, 'Science Fiction'), (10, 'Romance'), (5, 'Drama'), (2, 'Animation'), (0, 'Other'), (12, 'Thriller'), (9, 'Horror'), (6, 'Experimental'), (1, 'Action')], default=0),
        ),
    ]