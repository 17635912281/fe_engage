from django.db import models

# Create your models here.


class Profession(models.Model):
    name = models.CharField(max_length=255)
    tier = models.CharField(max_length=255)
    unit_type = models.CharField(max_length=255)
    precondition = models.CharField(max_length=255, blank=True)
    promotion = models.CharField(max_length=255, blank=True)
    vocational_skill = models.CharField(max_length=255, blank=True)
    weapon_aptitude_1 = models.CharField(max_length=255)
    weapon_aptitude_2 = models.CharField(max_length=255, blank=True)
    weapon_aptitude_3 = models.CharField(max_length=255, blank=True)
    weapon_level_1 = models.CharField(max_length=255)
    weapon_level_2 = models.CharField(max_length=255, blank=True)
    weapon_level_3 = models.CharField(max_length=255, blank=True)


    class Meta:
        db_table = 't_profession'

    
class ProfessionGrowths(models.Model):
    name = models.CharField(max_length=255)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name="profession_growths")
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
        db_table = 't_profession_growths'