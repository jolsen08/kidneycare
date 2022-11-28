# Generated by Django 4.1.2 on 2022-11-28 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition_stage', models.IntegerField()),
                ('sodium_recommendation', models.IntegerField()),
                ('protein_recommendation', models.IntegerField()),
                ('potassium_recommendation', models.IntegerField()),
                ('phosphorus_recommendation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('date_consumed', models.DateField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('highbloodpressure', models.BooleanField()),
                ('diabetes', models.BooleanField()),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.condition')),
            ],
        ),
    ]