# Generated by Django 4.1.2 on 2022-11-28 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_condition_water_recommendation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='condition',
            old_name='phosphorus_recommendation',
            new_name='phosphorus_recommendation_mg',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='potassium_recommendation',
            new_name='potassium_recommendation_mg',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='protein_recommendation',
            new_name='protein_recommendation_g_per_kg_body_weight',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='sodium_recommendation',
            new_name='sodium_recommendation_mg',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='water_recommendation',
            new_name='water_recommendation_L',
        ),
    ]
