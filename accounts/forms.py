from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import UserPost

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label="رمز عبور", widget=forms.PasswordInput)
    password2 = forms.CharField(label="تکرار رمز عبور", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean_username(self):
        username = self.cleaned_data["username"].strip()
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("این نام‌کاربری قبلاً استفاده شده است.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("این ایمیل قبلاً ثبت شده است.")
        return email

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password1")
        p2 = cleaned.get("password2")
        if p1 and p2 and p1 != p2:
            self.add_error("password2", "تکرار رمز عبور مطابقت ندارد.")
        return cleaned


class LoginForm(forms.Form):
    username_or_email = forms.CharField(label="نام‌کاربری یا ایمیل")
    password = forms.CharField(label="رمز عبور", widget=forms.PasswordInput)


class ProfileEditForm(forms.ModelForm):
    password1 = forms.CharField(label="رمز عبور جدید", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="تکرار رمز عبور جدید", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ["username", "email", "address"]

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        qs = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("این ایمیل قبلاً استفاده شده است.")
        return email

    def clean(self):
        cleaned = super().clean()
        p1, p2 = cleaned.get("password1"), cleaned.get("password2")
        if p1 or p2:
            if p1 != p2:
                self.add_error("password2", "رمزهای عبور یکی نیستند.")
            elif len(p1) < 8:
                self.add_error("password1", "رمز عبور باید حداقل ۸ کاراکتر باشد.")
        return cleaned

class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["avatar"]

    def clean_avatar(self):
        avatar = self.cleaned_data.get("avatar")
        if avatar:
            if avatar.size > 2 * 1024 * 1024:
                raise forms.ValidationError("حجم فایل باید کمتر از ۲ مگابایت باشد.")
            if not avatar.content_type in ["image/jpeg", "image/png", "image/gif"]:
                raise forms.ValidationError("فرمت فایل فقط باید JPEG یا PNG یا GIF باشد.")
        return avatar


class PostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ["title", "content"]