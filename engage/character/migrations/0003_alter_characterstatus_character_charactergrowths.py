# Generated by Django 4.2.7 on 2023-11-09 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0002_alter_character_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterstatus',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='character.character'),
        ),
        migrations.CreateModel(
            name='CharacterGrowths',
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
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='growths', to='character.character')),
            ],
            options={
                'db_table': 't_character_growths',
            },
        ),
    ]
