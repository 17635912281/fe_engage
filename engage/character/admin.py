from django.contrib import admin

# Register your models here.
from .models import Character, CharacterStatus, CharacterGrowths

admin.site.register(Character)
admin.site.register(CharacterStatus)
admin.site.register(CharacterGrowths)