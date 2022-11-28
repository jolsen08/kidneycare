# Generated by Django 4.1.2 on 2022-11-28 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_rename_phosphorus_recommendation_mg_condition_phosphorus_recommendation_mg_max_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='condition',
            old_name='water_recommendation_L_max',
            new_name='water_recommendation_L_max_men',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='water_recommendation_L_min',
            new_name='water_recommendation_L_max_women',
        ),
        migrations.AddField(
            model_name='condition',
            name='water_recommendation_L_min_men',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='condition',
            name='water_recommendation_L_min_women',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
