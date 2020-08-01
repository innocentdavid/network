
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("page/<int:pg>", views.page, name="page"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("vote", views.vote, name="vote"),
    path("profile/<str:user_id>/<int:pg>", views.profile, name="profile"),
    path("follow", views.follow, name="follow"),
    path("following/page/<int:pg>", views.following, name="following"),
    path("get_post/<str:id>", views.get_post, name="get_post"),
    path("update_post", views.update_post, name="update_post")
]
