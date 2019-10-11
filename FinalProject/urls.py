"""FinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from game_backend.views import main_page, design_game, admin_comments_review, admin_user_review, all_users, all_games, add_friend, user_review
from game_backend.views import get_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', main_page),
                  path('design-game/', design_game, name='design'),
                  path('admin-comment-review/', admin_comments_review),
                  path('admin-user-review/', admin_user_review),
                  path('all-users/', all_users),
                  path('all-games/', all_games, name='all-games'),
                  path('profile/', get_profile),
                  path('profile/<int:id>/', get_profile),
                  path('add_friend/', add_friend, name='add-friend'),
                  path('user_review/', user_review, name='user-review'),
                  path('accounts/', include('django.contrib.auth.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

