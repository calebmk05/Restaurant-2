# Generated by Django 5.0.3 on 2024-04-01 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_recipe_ingredients_recipe_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='Ingredients',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='Method',
        ),
    ]
