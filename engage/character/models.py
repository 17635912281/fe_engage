from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=255)
    internal_level = models.IntegerField(default=1)
    nationality = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    birthday = models.CharField("birthday", max_length=255)
    age = models.IntegerField()
    original_sp = models.IntegerField()
    personal_skill = models.CharField(max_length=255)
    weapon_aptitude_1 = models.CharField(max_length=255)
    weapon_aptitude_2 = models.CharField(max_length=255, blank=True)


    class Meta:
        db_table = "t_character"


class CharacterStatus(models.Model):
    name = models.CharField(max_length=255)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="status")
    level = models.IntegerField()
    hp = models.IntegerField()
    strong = models.IntegerField()
    magic = models.IntegerField()
    dexterity = models.IntegerField()
    speed = models.IntegerField()
    defense = models.IntegerField()
    resistance = models.IntegerField()
    lucky = models.IntegerField()
    build = models.IntegerField()
    movement = models.IntegerField()

    class Meta:
        db_table = 't_character_status'


class CharacterGrowths(models.Model):
    name = models.CharField(max_length=255)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="character_growths")
    hp = models.FloatField()
    strong = models.FloatField()
    magic = models.FloatField()
    dexterity = models.FloatField()
    speed = models.FloatField()
    defense = models.FloatField()
    resistance = models.FloatField()
    lucky = models.FloatField()
    build = models.FloatField()
    movement = models.FloatField()


    class Meta:
        db_table = 't_character_growths'

