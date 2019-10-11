from django.contrib import admin
from game_backend.models import Profile, GameLog, GameReview , UserReview, Friend
from game_backend.models import Game

class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)

class GameLogAdmin(admin.ModelAdmin):
    pass
admin.site.register(GameLog, GameLogAdmin)

class GameReviewAdmin(admin.ModelAdmin):
    pass
admin.site.register(GameReview, GameReviewAdmin)

class UserReviewAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserReview, UserReviewAdmin)

class GameAdmin(admin.ModelAdmin):
    pass

class FriendAdmin(admin.ModelAdmin):
    pass

admin.site.register(Friend, FriendAdmin)