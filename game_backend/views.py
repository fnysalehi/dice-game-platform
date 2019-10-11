from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from game_backend.models import Profile, GameReview, UserReview, Game, Friend
from django.contrib.auth.models import User
import json

def main_page(request):
    is_login = request.user.is_authenticated
    is_admin = request.user.is_staff
    user_review = []
    user_games = []
    user_friend_regs = []
    profile = None
    if is_login:
        if is_admin:

            template = loader.get_template('admin.html')
        else:
            print(len(user_review))
            user = User.objects.get(id=request.user.id)
            profile = Profile.objects.get(user=user)
            user_games = Game.objects.filter(player=profile)

            user_review = UserReview.objects.filter(publish=True).filter(target=profile)
            template = loader.get_template('registerd_user.html')
    else:
        template = loader.get_template('guest.html')

    online_users = Profile.objects.filter(is_online=True)

    top_game = Game.objects.all().order_by('game_score').first()
    newest_game = Game.objects.all().order_by('-date_added').first()
    online_game = Game.objects.all().order_by('online_player').first()
    user_friend_regs = Friend.objects.filter(friend_player=profile).filter(is_accepted=False)
    game_played = 0

    for game in user_games:
        game_played += game.online_player

    context = {"online_users" : online_users[:4],
               "top_game":top_game,
               "top_disc":"Review score: {}".format(top_game.game_score),
               "newest_game":newest_game,
               "newest_disc":"Time of design: {}".format(newest_game.date_added),
               "online_game":online_game,
               "online_disc":"Number of player: {}".format(online_game.online_player),
               "profile":profile,
               "user_review": user_review,
               "false": False,
               "user_games": user_games,
               "create_len": len(user_games),
               "game_played": game_played,
               "user_friend_regs": user_friend_regs,
               }
    return HttpResponse(template.render(context, request))

def design_game(request):
    template = loader.get_template('game_design.html')
    context = {}
    if request.method == 'POST':
        new_game = Game()
        new_game.max_score = request.POST.get('max_score')
        new_game.shut_out_dice = request.POST.get('shut_out_dice')
        new_game.dice_number = request.POST.get('dice_number')
        new_game.player = request.user.profile
        new_game.save()
        return HttpResponseRedirect(reverse('all-games'))

    return HttpResponse(template.render(context, request))

def admin_comments_review(request):
    template = loader.get_template('admin-commnet-review.html')
    reviews_user = GameReview.objects.filter(publish=True).order_by('player__user_id')
    reviews_date = GameReview.objects.filter(publish=True).order_by('-date_added')
    context = {
        'reviews_user':reviews_user,
        'reviews_date':reviews_date,
    }
    return HttpResponse(template.render(context, request))

def admin_user_review(request):
    template = loader.get_template('admin-user-review.html')
    reviews_user = UserReview.objects.filter(publish=True).order_by('publisher__user_id')
    reviews_date = UserReview.objects.filter(publish=True).order_by('-date_added')
    context = {
        'reviews_user': reviews_user,
        'reviews_date': reviews_date,
    }
    return HttpResponse(template.render(context, request))

def all_users(request):
    template = loader.get_template('all_users.html')
    users_newest = Profile.objects.all().order_by('-date_added')
    users_score = Profile.objects.all().order_by('-score')
    users_play = Profile.objects.all().order_by('-game_count')
    context = {
        'users_newest': users_newest,
        'users_score': users_score,
        'users_play': users_play,
               }
    return HttpResponse(template.render(context, request))

def all_games(request):
    template = loader.get_template('all_games.html')
    games_newest = Game.objects.all().order_by('-date_added')
    games_fastest = Game.objects.all().order_by('max_score')
    games_dice = Game.objects.all().order_by('-dice_number')
    context = {
        'games_newest': games_newest,
        'games_fastest': games_fastest,
        'games_dice': games_dice,
    }
    return HttpResponse(template.render(context, request))

def get_profile(request, id=None):
    template = loader.get_template('profile.html')
    if id:
        profile = Profile.objects.get(id=id)
    else:
        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user=user)
    context = {'profile' : profile}
    return HttpResponse(template.render(context, request))


def add_friend(request):
    friendship = Friend()
    friendship.player = request.user.profile
    friendship.friend_player = Profile.objects.get(id=request.POST.get('friend_player_id'))
    friendship.save()
    return JsonResponse({'status': 'ok'})



def user_review(request):
    user_review = UserReview()
    user_review.score = request.POST.get('score')
    user_review.comment = request.POST.get('comment')
    user_review.target = Profile.objects.get(id=request.POST.get('target_player_id'))
    user_review.publisher = request.user.profile
    user_review.save()
    return JsonResponse({'status': 'ok'})
