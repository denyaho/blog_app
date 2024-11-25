from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from mysite.models.account_models import User
from mysite.models.profile_models import Profile
from django.contrib.auth.models import Group
# Register your models here.
from mysite.forms import UserCreationForm


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
#    verbose_name_plural = "Profile"


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    fieldsets = (
        (None,{
            "fields": (
                "email",
                "password",
                )
        }),
        (None,{
            "fields": (
                "is_active",
                "is_admin",
            )
            })
    )

    list_display = ("email","is_active")
    list_filter = ()
    ordering = ()
    filter_horizontal = ()

    add_fieldsets = (
        (None, {
            "fields": ("email","password",),
        })
    )

    add_form = UserCreationForm

admin.site.unregister(Group) #表示されなくする
admin.site.register(User,CustomUserAdmin)
