""" User admin classes """

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User

# Models
from users.models import Profile
from django.contrib.auth.models import User

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  """ Profile Admin """

  list_display  = (
    # 'pk',
    'user',
    'phone_number',
    'website',
    'picture',
  )

  list_display_links = (
    # 'pk',
    'user',
    'phone_number'
  )

  search_fields = (
    'user__username',
    'user__email',
    'user__first_name',
    'user__last_name',
    'phone_number'
  )

  list_filter = (
    'created_at',
    'modified_at',
    'user__is_active',
    'user__is_staff'
  )

  fieldsets = (
    ('Perfil', {
      'fields': ('user','picture')
    }),
    ('Información extra', {
      'fields': (
        ('website','phone_number'),
        ('biography')
      )
    }),
    ('Metadata', {
      'fields':('created_at', 'modified_at')
    }),
  )

  readonly_fields = ('created_at','modified_at','user')


class ProfileInline(admin.StackedInline):
  model = Profile
  can_delete = False
  verbose_name = 'Perfil'
  verbose_name_plural = 'Perfiles'

class UserAdmin(BaseUserAdmin):
  inlines = (ProfileInline,)
  list_display = (
    'username',
    'email',
    'first_name',
    'last_name',
    'is_active',
    'is_staff'
  )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


