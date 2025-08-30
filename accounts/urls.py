from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.accounts_home, name="home"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("profile/", views.profile_view, name="profile"),
    path("profile/edit/", views.edit_profile_view, name="edit_profile"),
    path("profile/avatar/", views.upload_avatar_view, name="upload_avatar"),
    path("profile/avatar/delete/", views.delete_avatar_view, name="delete_avatar"),
    path("posts/create/", views.create_post_view, name="create_post"),
    path("posts/<int:post_id>/edit/", views.edit_post_view, name="edit_post"),
    path("posts/<int:post_id>/delete/", views.delete_post_view, name="delete_post"),
]