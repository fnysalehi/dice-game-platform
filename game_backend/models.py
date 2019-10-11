from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    game_count = models.IntegerField(default=0, blank=False, null=False)
    win_count = models.IntegerField(default=0, blank=False, null=False)
    designed_game_count = models.IntegerField(default=0, blank=False, null=False)
    score = models.IntegerField(default=0, blank=False, null=False)
    is_online = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='static/img/list-icons',
                               blank=True,
                               null=True,
                               verbose_name="avatar")
    date_added = models.DateField()

class GameLog(models.Model):
    winner = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='winner')
    loser = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='loser')
    score = models.IntegerField(blank=False, null=False)
    date_added = models.DateField()

class GameReview(models.Model):
    player = models.OneToOneField(Profile, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    publish = models.BooleanField(default=False)
    date_added = models.DateField()

class UserReview(models.Model):
    target = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='target')
    publisher = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='publisher')
    score = models.IntegerField(blank=False, null=False)
    comment = models.CharField(max_length=500, blank=True)
    publish = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)

class Game(models.Model):
    max_score = models.IntegerField(default=100)
    shut_out_dice = models.IntegerField(default=1)
    dice_number = models.IntegerField(default=1)
    player = models.ForeignKey(Profile, on_delete=models.CASCADE)
    online_player = models.IntegerField(default=0)
    game_score = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)

class Friend(models.Model):
    player = models.ForeignKey(Profile, on_delete=models.CASCADE)
    friend_player = models.ForeignKey(Profile, related_name='friend_player', on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
