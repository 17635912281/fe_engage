# Generated by Django 4.2.7 on 2023-11-09 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0008_alter_character_weapon_aptitude_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='weapon_aptitude_1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='character',
            name='weapon_aptitude_2',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]