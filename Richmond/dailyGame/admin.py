from django.contrib import admin
from .models import Game, JoinedPlayer, GameRecord

admin.site.register(Game)
admin.site.register(JoinedPlayer)
admin.site.register(GameRecord)