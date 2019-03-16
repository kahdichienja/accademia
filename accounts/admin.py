from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
# Register your models here.
User = get_user_model()


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm #update/edit view
    add_form = UserAdminCreationForm #create view

    list_display = ('email', 'admin')
    list_filter = ('admin', 'staff', 'active')
    list_display = ["username", "admission_number","university","email","phone_number"]

    fieldsets = (
        (None, {'fields': ('email', 'password')}),#'full_name', 
        # if you need to organise inform of tabs in the admin site.>>>>>
        ('Personal Info', {'fields': ('full_name','phone_number', 'username','admission_number', 'university',)}),#'full_name',
        ('Permissions', {'fields': ('admin', 'staff', 'active',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('email', 'password1', 'password2')
        }),
    )
    search_fields = ('email','admission_number',)#'full_name',
    ordering = ('email',)
    filter_horizontal = ()

# class UserAdmin(admin.ModelAdmin):
#     search_fields = ['email']
#     form = UserAdminChangeForm #update/edit view
#     add_form = UserAdminCreationForm #create view
#     # class Meta:
#     #     model = User
admin.site.register(User, UserAdmin)

# remove the group
admin.site.unregister(Group)