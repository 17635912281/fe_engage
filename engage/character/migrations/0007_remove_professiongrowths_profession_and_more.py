# Generated by Django 4.2.7 on 2023-11-09 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0006_profession_character_internal_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professiongrowths',
            name='profession',
        ),
        migrations.DeleteModel(
            name='Profession',
        ),
        migrations.DeleteModel(
            name='ProfessionGrowths',
        ),
    ]