# Django
from django.contrib import admin
from django.db import models

# Local
from request.models import CategoryService, ComponentType, Entity, Letter, LetterService, Service

# Register your models here.
@admin.register(CategoryService)
class CategoryServiceAdmin (admin.ModelAdmin):

  list_display = (
    'id',
    'description',
  )

  list_display_links = (
    'id',
    'description',
  )

  search_fields = (
    'description',
  )

  fieldsets = (
    ('Categoría de servicio', {
      'fields': ('description',)
    }),
    ('Metadata', {
      'fields':(
        'user_id',
        'created_at', 
        'modified_at'
      )
    }),
  )

  readonly_fields = ('created_at','modified_at','user_id')

  def save_model(self, request, obj, form, change) -> None:
      obj.user_id = request.user.username
      return super().save_model(request, obj, form, change)

  readonly_fields = ('created_at','modified_at','user_id')

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'description',
  )   

  list_display_links  = (
    'id',
    'description',
  )  

  search_fields = ('description',)

  fieldsets = (
    ('Carta', {
      'fields' : ('description','letter_text')
    }),
    ('Metadata', {
      'fields': (
        'user_id',
        'created_at', 
        'modified_at'
    )
    })
  )

  readonly_fields = ('created_at','modified_at','user_id')

  def save_model(self, request, obj, form, change) -> None:
      obj.user_id = request.user.username
      return super().save_model(request, obj, form, change)

@admin.register(LetterService)
class LetterServiceAdmin(admin.ModelAdmin):
  list_display = (
    'description',
    'service',
    'letter',
    'order_display',
  )

  list_display_links  = (
    'description',
    'service',
    'letter',
    'order_display',
  )  

  search_fields = ('service__description', 'letter__description','description')

  fieldsets = (
    ('Condiciones de servicios', {
      'fields' : ('description','service','letter','order_display',)
    }),
    ('Metadata', {
      'fields': (
        'user_id',
        'created_at', 
        'modified_at',
      )
    })
  )

  readonly_fields = ('created_at','modified_at','user_id')

  def save_model(self, request, obj, form, change) -> None:
      obj.user_id = request.user.username
      return super().save_model(request, obj, form, change)

@admin.register(ComponentType)
class ComponentTypeAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'description',
  )

  list_display_links = (
    'id',
    'description',
  )

  search_fields = ('description',)

  readonly_fields = ('created_at','modified_at','user_id')

  fieldsets = (
    ('Componente', {
      'fields' : ('description',)
    }),
    ('Metadata', {
      'fields': (
        'user_id',
        'created_at', 
        'modified_at',
      )
    })
  )

  def save_model(self, request, obj, form, change) -> None:
      obj.user_id = request.user.username
      return super().save_model(request, obj, form, change)
@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
  list_display = (
    'description',
    'email',
    'root_entity'
  )

  list_display_links = (
    'description',
    'email',
    'root_entity'
  )

  search_fields = ('description', 'root_entity__description')

  fieldsets = (
    ('Datos entidades', {
      'fields' : ('description','email','root_entity')
    }),
    ('Metadata', {
      'fields': (
        'user_id',
        'created_at', 
        'modified_at',
      )
    })
  )

  list_filter = ('root_entity__description',)

  readonly_fields = ('created_at','modified_at','user_id')

  def save_model(self, request, obj, form, change) -> None:
      obj.user_id = request.user.username
      return super().save_model(request, obj, form, change)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'description',
    'web_indicator',
    'category_service',
    'entity'
  )

  list_display_links = (
    'id',
    'description',
  )

  search_fields = (
    'description',
    'category_service__description',
    'entity__description'
  )

  list_filter = ('web_indicator',)

  fieldsets = (
    ('Servicio', {
      'fields': (('description','category_service'), 
                 ('entity','web_indicator'))
    }),
    ('Metadata', {
      'fields':(
        'user_id',
        'created_at', 
        'modified_at'
      )
    }),
  )

  readonly_fields = ('created_at','modified_at','user_id')

  def save_model(self, request, obj, form, change) -> None:
      obj.user_id = request.user.username
      return super().save_model(request, obj, form, change)      
  
  


