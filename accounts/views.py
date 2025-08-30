from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import RegistrationForm, LoginForm, ProfileEditForm, AvatarUploadForm, PostForm
from .models import Role, UserPost
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


User = get_user_model()

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]

            user = User.objects.create_user(username=username, email=email, password=password)

            try:
                default_role = Role.objects.get(name="user")
                user.role = default_role
                user.save()
            except Role.DoesNotExist:
                pass

            messages.success(request, "ثبت‌نام موفقیت‌آمیز بود. حالا می‌تونی وارد بشی.")
            return redirect("accounts:login")
    else:
        form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            ue = form.cleaned_data["username_or_email"]
            password = form.cleaned_data["password"]

            if "@" in ue:
                try:
                    ue = User.objects.get(email__iexact=ue).username
                except User.DoesNotExist:
                    pass

            user = authenticate(request, username=ue, password=password)
            if user:
                login(request, user)
                messages.success(request, f"خوش آمدی {user.username}!")
                return redirect("accounts:dashboard")
            else:
                messages.error(request, "نام کاربری/ایمیل یا رمز اشتباه است.")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "خارج شدی.")
    return redirect("accounts:login")


def dashboard_view(request):
    if not request.user.is_authenticated:
        messages.warning(request, "لطفاً ابتدا وارد شوید.")
        return redirect("accounts:login")
    return render(request, "accounts/dashboard.html")

@login_required
def profile_view(request):
    posts = UserPost.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "accounts/profile.html", {
        "user": request.user,
        "posts": posts
    })

@login_required
def edit_profile_view(request):
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data.get("password1"):
                user.set_password(form.cleaned_data["password1"])
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, "پروفایل با موفقیت ویرایش شد.")
            return redirect("accounts:profile")
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, "accounts/edit_profile.html", {"form": form})

def accounts_home(request):
    return render(request, "accounts/home.html")


@login_required
def upload_avatar_view(request):
    if request.method == "POST":
        form = AvatarUploadForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile")
    else:
        form = AvatarUploadForm(instance=request.user)
    return render(request, "accounts/upload_avatar.html", {"form": form})


@login_required
def delete_avatar_view(request):
    if request.user.avatar:
        request.user.avatar.delete(save=True)
    return redirect("accounts:profile")


@login_required
def create_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("accounts:profile")
    else:
        form = PostForm()
    return render(request, "accounts/create_post.html", {"form": form})

@login_required
def edit_post_view(request, post_id):
    post = get_object_or_404(UserPost, id=post_id, user=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile")
    else:
        form = PostForm(instance=post)
    return render(request, "accounts/edit_post.html", {"form": form})


@login_required
def delete_post_view(request, post_id):
    post = get_object_or_404(UserPost, id=post_id, user=request.user)
    if request.method == "POST":  # تایید حذف
        post.delete()
        return redirect("accounts:profile")
    return render(request, "accounts/confirm_delete.html", {"post": post})



