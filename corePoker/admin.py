from django.contrib import admin

from corePoker.models import Game


# Register your models here.

class GameAdmin(admin.ModelAdmin):
    fields = ["name","winner","fase"]



admin.site.register(Game, GameAdmin)