from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserCreationForm

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    
    list_display = ('username', 'email', 'position', 'is_admin', 'is_creater')
    list_filter = ('is_admin',)
    readonly_fields = ('id', 'date_joined', 'last_login')

    fieldsets = (
        (None, {'fields' : ('email', 'username', 'position', 'password')}),
        ('Permissions', {'fields' : ('is_admin', 'is_creater')})
    )

    search_fields = ('email', 'username')
    ordering = ('username', 'email')

    filter_horizontal = ()

admin.site.register(User, UserAdmin)