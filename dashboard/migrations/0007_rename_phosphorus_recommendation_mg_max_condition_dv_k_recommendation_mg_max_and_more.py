# Generated by Django 4.1.2 on 2022-11-28 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_rename_water_recommendation_l_max_condition_water_recommendation_l_max_men_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='condition',
            old_name='phosphorus_recommendation_mg_max',
            new_name='dv_k_recommendation_mg_max',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='phosphorus_recommendation_mg_min',
            new_name='dv_k_recommendation_mg_min',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='potassium_recommendation_mg_max',
            new_name='dv_phos_recommendation_mg_max',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='potassium_recommendation_mg_min',
            new_name='dv_phos_recommendation_mg_min',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='protein_recommendation_g_per_kg_body_weight',
            new_name='dv_protein_recommendation_g_per_kg_body_weight',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='sodium_recommendation_mg_max',
            new_name='dv_sodium_recommendation_mg_max',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='sodium_recommendation_mg_min',
            new_name='dv_sodium_recommendation_mg_min',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='water_recommendation_L_max_men',
            new_name='dv_water_recommendation_L_max_men',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='water_recommendation_L_max_women',
            new_name='dv_water_recommendation_L_max_women',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='water_recommendation_L_min_men',
            new_name='dv_water_recommendation_L_min_men',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='water_recommendation_L_min_women',
            new_name='dv_water_recommendation_L_min_women',
        ),
        migrations.AddField(
            model_name='condition',
            name='serum_albuminmg_per_dL_max',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='condition',
            name='serum_albuminmg_per_dL_min',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='condition',
            name='serum_blood_sugar_mg_per_dL_max',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='condition',
            name='serum_blood_sugar_mg_per_dL_min',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='condition',
            name='serum_creatinine_mg_per_dL_men',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='condition',
            name='serum_creatinine_mg_per_dL_women',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='condition',
            name='serum_k_mg_per_dL_max',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='condition',
            name='serum_k_mg_per_dL_min',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='condition',
            name='serum_na_mEq_per_L_min',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='condition',
            name='serum_phos_mg_per_dL_max',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='condition',
            name='serum_phos_mg_per_dL_min',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]