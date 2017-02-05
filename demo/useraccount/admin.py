
# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile,Apartments,Apartment_images


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
##admin.site.unregister(Apartments)
admin.site.register(Apartments)
##admin.site.unregister(Apartment_images)
admin.site.register(Apartment_images)
