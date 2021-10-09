from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Admin


class CustomUserAdmin(admin.ModelAdmin):
    model = Admin
    list_display = ('surname', 'name', 'email')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Инфо', {'fields': ('surname', 'name')}),
        ('Данные', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'), }),
        ('Инфо', {
            'classes': ('wide',),
            'fields': ('surname', 'name')}),
    )
    readonly_fields = ('last_login',)
    search_fields = ('email', 'name', 'surname')
    ordering = ('email',)


admin.site.register(Admin, CustomUserAdmin)

admin.site.unregister(Group)
