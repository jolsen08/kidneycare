# Generated by Django 4.1.2 on 2022-11-28 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_rename_phosphorus_recommendation_condition_phosphorus_recommendation_mg_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='condition',
            old_name='phosphorus_recommendation_mg',
            new_name='phosphorus_recommendation_mg_max',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='potassium_recommendation_mg',
            new_name='phosphorus_recommendation_mg_min',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='sodium_recommendation_mg',
            new_name='potassium_recommendation_mg_max',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='water_recommendation_L',
            new_name='water_recommendation_L_max',
        ),
        migrations.AddField(
            model_name='condition',
            name='potassium_recommendation_mg_min',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='condition',
            name='sodium_recommendation_mg_max',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='condition',
            name='sodium_recommendation_mg_min',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='condition',
            name='water_recommendation_L_min',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]