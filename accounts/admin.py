from django.contrib import admin
from .models import User, Role, UserRole

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','role','created_at','updated_at','is_staff')
    search_fields = ('username','email')
    list_filter = ('role','is_staff')

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('id','user','role')
