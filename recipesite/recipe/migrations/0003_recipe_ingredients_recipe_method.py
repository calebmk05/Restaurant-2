# Generated by Django 5.0.3 on 2024-04-01 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_holidaymeal_mealdiet_mealtype_recipe_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='method',
            field=models.TextField(null=True),
        ),
    ]
