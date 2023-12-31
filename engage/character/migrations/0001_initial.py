# Generated by Django 4.2.7 on 2023-11-08 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=255)),
                ('birthday', models.DateTimeField(verbose_name='birthday')),
                ('age', models.IntegerField()),
                ('original_sp', models.IntegerField()),
                ('personal_skill', models.CharField(max_length=255)),
                ('weapon_aptitude_1', models.CharField(max_length=255)),
                ('weapon_aptitude_2', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 't_character',
            },
        ),
        migrations.CreateModel(
            name='CharacterStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('strong', models.IntegerField()),
                ('magic', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('resistance', models.IntegerField()),
                ('lucky', models.IntegerField()),
                ('build', models.IntegerField()),
                ('movement', models.IntegerField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.character')),
            ],
            options={
                'db_table': 't_character_status',
            },
        ),
    ]
