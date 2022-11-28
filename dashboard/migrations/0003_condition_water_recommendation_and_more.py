# Generated by Django 4.1.2 on 2022-11-28 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_height_person_height_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='water_recommendation',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='condition',
            name='sodium_recommendation',
            field=models.IntegerField(),
        ),
    ]