# Generated by Django 4.1.2 on 2022-11-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_foodconsumption'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='food_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
