from django.urls import path, reverse
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from customuser.models import UserManager

from .forms import UserAdminCreationForm, UserAdminChangeForm

from .models import Address
User = get_user_model()

# Supprimer le modèle de groupe de l'administrateur. Nous ne l'utilisons pas.
# admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    # Les formulaires pour ajouter et modifier des instances d'utilisateur
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # Les champs à utiliser pour afficher le modèle User.
    # Celles-ci remplacent les définitions de la baseUserAdmin
    # qui font référence à des champs spécifiques sur auth.User.
    list_display = ['email', 'admin', 'staff']
    list_filter = ['admin', 'groups', 'user_permissions']
    fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ('Personal info', {'fields': ( 'firstname', 'lastname', 'phone',)}),
    ('Permissions', {'fields': ('staff','admin','is_active', 'groups', 'user_permissions')}),
    )
    # add_fieldsets n'est pas un attribut ModelAdmin standard. UtilisateurAdmin
    # remplace get_fieldsets pour utiliser cet attribut lors de la création d'un utilisateur.
    add_fieldsets = (
    (None, {
    'classes': ('wide',),
    'fields': ('email', 'password', 'password_2','firstname', 'lastname', 'phone',)}
    ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ('groups', 'user_permissions',)
    



admin.site.register(User, UserAdmin)
admin.site.register(Address)