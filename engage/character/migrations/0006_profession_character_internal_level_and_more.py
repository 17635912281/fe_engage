# Generated by Django 4.2.7 on 2023-11-09 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0005_alter_charactergrowths_build_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('precondition', models.CharField(max_length=255)),
                ('vocational_skill', models.CharField(max_length=255)),
                ('weapon_aptitude_1', models.CharField(max_length=255)),
                ('weapon_aptitude_2', models.CharField(max_length=255)),
                ('weapon_aptitude_3', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 't_profession',
            },
        ),
        migrations.AddField(
            model_name='character',
            name='internal_level',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='charactergrowths',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_growths', to='character.character'),
        ),
        migrations.CreateModel(
            name='ProfessionGrowths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('hp', models.FloatField()),
                ('strong', models.FloatField()),
                ('magic', models.FloatField()),
                ('dexterity', models.FloatField()),
                ('speed', models.FloatField()),
                ('defense', models.FloatField()),
                ('resistance', models.FloatField()),
                ('lucky', models.FloatField()),
                ('build', models.FloatField()),
                ('movement', models.FloatField()),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profession_growths', to='character.profession')),
            ],
            options={
                'db_table': 't_profession_growths',
            },
        ),
    ]
