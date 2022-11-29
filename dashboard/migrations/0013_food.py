# Generated by Django 4.1.2 on 2022-11-29 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_person_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dv_sodium_mg', models.IntegerField()),
                ('dv_protein_g_per_kg_body_weight', models.FloatField()),
                ('dv_water_L', models.FloatField()),
                ('dv_k_mg', models.IntegerField()),
                ('dv_phos_mg', models.IntegerField()),
                ('person', models.ManyToManyField(to='dashboard.person')),
            ],
        ),
    ]