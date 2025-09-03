from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("", views.accounts_home, name="home"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("home/", views.home_view, name="home"),
    path("profile/", views.profile_view, name="profile"),
    path("profile/edit/", views.edit_profile_view, name="edit_profile"),
    path("profile/avatar/", views.upload_avatar_view, name="upload_avatar"),
    path("profile/avatar/delete/", views.delete_avatar_view, name="delete_avatar"),
    path("posts/create/", views.create_post_view, name="create_post"),
    path("posts/<int:post_id>/edit/", views.edit_post_view, name="edit_post"),
    path("posts/<int:post_id>/delete/", views.delete_post_view, name="delete_post"),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),
    path("posts/<int:post_id>/like/", views.like_post, name="like_post"),
    path("search/", views.search_posts, name="search_posts"),

    path(
        "password_reset/",
         auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset.html",
            email_template_name="accounts/password_reset_email.html",
            success_url=reverse_lazy("accounts:password_reset_done")
         ),
         name="password_reset"
    ),
    path(
        "password_reset/done/",
         auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
         ),
         name="password_reset_done"
    ),
    path(
        "reset/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url=reverse_lazy("accounts:password_reset_complete")
         ),
         name="password_reset_confirm"
    ),
    path(
        "reset/done/",
         auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
         ),
         name="password_reset_complete"
    ),
]