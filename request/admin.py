# Django
from colorfield.fields import ColorField
from django.forms import Textarea
from django import forms
from django.contrib import admin
from django.db import models
from django.db.models.aggregates import Max
from django.db.models.fields import TextField
from django.forms import formsets
from django.forms.fields import TypedChoiceField

# Local
from request.models import CategoryService, CommunicationChannel, ComponentSubsection, ComponentType, ConfigVariable, DataSource, DataSourceValue, Entity, FooterWeb, Letter, LetterService, MainFormSection, MainSection, Priority, RequestBody, RequestHeader, RequestHistory, Service, ServiceConfiguration, ServiceConfigurationStatus, Status, Subsection, subsectionServiceForm

# Register your models here.
@admin.register(CategoryService)
class CategoryServiceAdmin (admin.ModelAdmin):

  list_display = (
    'description',
  )

  list_display_links = (
    'description',
  )

  search_fields = (
    'description',
  )

  ordering = ('description',)

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
    ('Marco legal', {
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
    'description',
  )

  list_display_links = (
    'description',
  )

  search_fields = ('description',)

  readonly_fields = ('created_at','modified_at','user_id')

  ordering = ('description',)

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

  list_filter = ('root_entity',)

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

@admin.register(FooterWeb)
class FooterWebAdmin(admin.ModelAdmin):

  list_display = (
    'description',
    'orientation',
    'order_display',
    'is_active'
  )  

  list_display_links = (
    'description',
  )

  search_fields = (
    'description',
  )

  list_filter = ('is_active',)

  fieldsets = (
    ('Datos del footer', {
      'fields': ('description',
                 ('orientation','order_display','is_active',),
                 'text_html',  )
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

@admin.register(MainSection)
class MainSectionAdmin(admin.ModelAdmin):

  list_display = (
    'description',
  )

  list_display_links = (
    'description',
  )

  search_fields = (
    'description',
  )

  ordering = ('description',)

  fieldsets = (
    ('Datos principales', {
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

  # list_per_page = 25

  readonly_fields = ('created_at','modified_at','user_id')

  def save_model(self, request, obj, form, change) -> None:
      obj.user_id = request.user.username
      return super().save_model(request, obj, form, change) 

@admin.register(Subsection)
class SubsectionAdmin(admin.ModelAdmin):

  list_display = (
    'description',
    'key_config',
  )

  list_display_links = (
    'description',
    'key_config',
  )

  search_fields = (
    'description',
  )

  ordering = ('description',)

  fieldsets = (
    ('Datos principales', {
      'fields': (
        'description',
        'key_config'),
    }),
    ('Metadata', {
      'fields':(
        'user_id',
        'created_at', 
        'modified_at'
      )
    }),
  )

  readonly_fields = ('created_at','modified_at','user_id',)

  def save_model(self, request, obj, form, change) -> None:
      obj.user_id = request.user.username
      return super().save_model(request, obj, form, change)

# @admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):

  list_display = (
    'source',
    'related_source'
  )

  list_display_links = (
    'source',
    'related_source'
  )

  search_fields = (
    'source',
    'related_source'
  )

  fieldsets = (
   ('Datos principales', {
     'fields': ('source', 'related_source',)
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

@admin.register(ConfigVariable)
class ConfigVariableAdmin(admin.ModelAdmin):

  list_display = (
    'code',
    'description',
    'sequence',
    'value',
    'system_required',
    'group_variable',
  )

  list_display_links = (
    'code',
    'description',
    'sequence',
    'value',
    'group_variable',
  )

  search_fields = (
    'code',
    'description',
    'group_variable',
  )

  ordering = ('group_variable','sequence',)

  fieldsets = (
   ('Datos principales', {
     'fields': ('code', 'description','value','sequence',
                'system_required','group_variable')
   }),
   ('Metadata', {
     'fields':(
       'user_id',
       'created_at', 
       'modified_at'
     )
   }),
  )

  readonly_fields = ('created_at','modified_at','user_id','sequence')

  def save_model(self, request, obj, form, change) -> None:

      try:
        sequence_max = ConfigVariable.objects.filter(group_variable=obj.group_variable)
        seq_max = sequence_max.aggregate(Max('sequence'))['sequence__max']
        seq_max = seq_max + 1
        obj.sequence = seq_max
      except:
        seq_max = 1
      obj.user_id = request.user.username
      return super().save_model(request, obj, form, change)

@admin.register(CommunicationChannel)
class CommunicationChannelAdmin(admin.ModelAdmin):

  list_display = (
    'code',
    'description'
  )

  list_display_links = (
    'code',
    'description'
  )

  fieldsets = (
   ('Datos principales', {
     'fields': ('code', 'description')
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

class DataSourceValueAdminInline(admin.TabularInline):

  model =  DataSourceValue
  fk_name = 'source_data'
  extra = 1

@admin.register(DataSource)
class DataSourceTabAdmin(admin.ModelAdmin):

  list_display = (
    'source',
    'related_source',
  )

  list_display_links = (
    'source',
    'related_source',
  )
  search_fields = (
    'source',
  )

  ordering = ('source',)

  fieldsets = (
   ('configuración de fuente de datos', {
     'fields': (
       'source', 
       'related_source',
     )
   }),
  )

  inlines = [DataSourceValueAdminInline,]

# class ServiceConfigurationAdmin(admin.ModelAdmin):

#   list_display = (
#     'rule_service',
#     'role_id',
#     'start_date',
#     'end_date',
#     'delivery_days',
#     'bussiness_days',
#     'is_active',
#     'is_payment',
#   )

#   list_display_links = (
#     'rule_service',
#     'role_id',
#     'start_date',
#     'end_date',
#     'delivery_days',
#     'bussiness_days',
#     'is_active',
#   )

#   fieldsets = (
#    ('Reglas de servicio', {
#      'fields': (
#        ('rule_service', 'role_id'),
#        ('population_filter_api',),
#        ('start_date', 'end_date'),
#        ('delivery_days','bussiness_days',),
#        ('is_active','is_payment',),
#        ('comments',),
#      )
#    }),
#    ('Metadata', {
#      'fields':(
#        'user_id',
#        'created_at', 
#        'modified_at'
#      )
#    }),
#   )

#   readonly_fields = ('created_at','modified_at','user_id')

#   def save_model(self, request, obj, form, change) -> None:

#     obj.user_id = request.user.username
#     return super().save_model(request, obj, form, change)

class MainFormSectionAdminInline(admin.TabularInline):

  model =  MainFormSection
  fk_name = 'rule_service'
  extra = 1

class FormSubsectionAdminInline(admin.TabularInline):

  model =  subsectionServiceForm
  fk_name = 'rule_service'
  extra = 1

class StatusServiceAdminInline(admin.TabularInline):
  model = ServiceConfigurationStatus
  fk_name = 'rule_service'
  extra = 1
  fields = (
    'status_request',
    'assign_to',
    'status_start',
    'status_finished',
  )

@admin.register(ServiceConfiguration)
class MainFormSectionTabAdmin(admin.ModelAdmin):
  
  list_display = (
    'service_id',
    'start_date',
    'end_date',
    'is_active',
    'is_payment',
    'is_form_active',
  )

  list_display_links = (
    'service_id',
    'start_date',
    'end_date',
    'is_active',
    'is_payment',
    'is_form_active',
  )

  search_fields = ('service_id__description',)

  ordering = (
    'service_id',
  )

  inlines = [
    MainFormSectionAdminInline,
    FormSubsectionAdminInline,
    StatusServiceAdminInline,
  ]

  fieldsets = (
   ('Reglas de servicio', {
     'fields': (
       ('service_id', 'role_id'),
       ('population_filter_api',),
       ('start_date', 'end_date'),
       ('delivery_days',),
       ('is_active',
        'is_form_active',
        'is_autenticado',
        'valid_user',
       ),
       ('bussiness_days',
        'working_hours', 
        'is_payment',),
       ('url_form',),
       ('days_validity_document', 'digital_document', 'physical_document',),
       ('generation_process','cost_of_service',),
       ('comments',),
     )
   }),
  )

  readonly_fields = ('created_at','modified_at','user_id')

  def save_model(self, request, obj, form, change) -> None:

    obj.user_id = request.user.username
    return super().save_model(request, obj, form, change)

# @admin.register(subsectionServiceForm)
class subsectionServiceFormAdmin(admin.ModelAdmin):

  list_display = (
    'rule_service',
    'subsection_service',
    'section_main_form',
    'is_active',
    'order_display',
  )

  list_display_links = (
    'rule_service',
    'subsection_service',
    'section_main_form',
  )

  readonly_fields = (
    'rule_service',
    'subsection_service',
    'section_main_form',
    'is_active',
    'order_display',
  )

class ComponentSubsectionAdminInline(admin.TabularInline):

  model =  ComponentSubsection
  fk_name = 'rule_subsection'
  extra = 1

@admin.register(subsectionServiceForm)
class rule_subsetionTabAdmin(admin.ModelAdmin):

  list_display = (
    'rule_service',
    'subsection_service',
    'section_main_form',
    'is_active',
    'order_display',
  )

  list_display_links = (
    'rule_service',
    'subsection_service',
    'section_main_form',
  )
  search_fields = (
    'rule_service',
    'subsection_service',
    'section_main_form',
  )

  readonly_fields = ('rule_service',
    'subsection_service',
    'section_main_form',
    'is_active',
    'order_display',
  )

  inlines = [
    ComponentSubsectionAdminInline,
    
  ]

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):

  list_display = (
    'description',
    'priority_percentage',
    'color_priority'
  )

  list_display_links = (
    'description',
    'priority_percentage',
    'color_priority'
  )

  fieldsets = (
   ('Datos de prioridad', {
     'fields': ('description',
      'priority_percentage',
      'color_priority',
     )
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

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):

  list_display = (
    'code',
    'description',
    'completion_status',
    'visible_state',
  )

  list_display_links = (
    'code',
    'description',
    'completion_status',
    'visible_state',
  )

  fieldsets = (
   ('Estado de solicitudes', {
     'fields': (('code','description',),
      ('completion_status', 'visible_state',),
     )
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

class RequestBodyAdminInline(admin.TabularInline):

  model = RequestBody
  fk_name = 'header_request_id'
  extra = 1

class RequestHistoryAdminInline(admin.TabularInline):
  
  model = RequestHistory
  fk_name = 'header_request_id'
  extra = 1

  formfield_overrides = {
    models.TextField: {'widget': Textarea (
                       attrs={'rows': 1,
                              'cols': 40})},
  }

@admin.register(RequestHeader)
class RequestHeaderTabAdmin(admin.ModelAdmin):
  
  list_display = (
    'id_usuario',
    'rule_service',
    'service',
    'status_service',
    'estimated_date',
    'document_type',
    'reception_date',
    'delivery_date'
  )

  list_display_links = (
    'id_usuario',
    'rule_service',
    'service',
    'status_service',
    'estimated_date',
    'document_type',
    'reception_date',
    'delivery_date',
  )

  list_filter = ('service__description', 'status_service')

  formfield_overrides = {
    models.TextField: {'widget': Textarea (
                       attrs={'rows': 1,
                              'cols': 120})},
  }

  search_fields = (
    'id_usuario',
  )

  # filter_horizontal = ('service',)

  inlines = [
    RequestBodyAdminInline,
    RequestHistoryAdminInline,
  ]

  fieldsets = (
   ('Encabezado de solicitud', {
     'fields': (
       ('id_usuario', 'email_applicant'),
       ('rule_service','service'),
       ('status_service','date_status_change','term_code'),
       ('reception_date', 'estimated_date','delivery_date'),
       ('document_type','communication_channel'),
       ('correspondence_address','copies'),
       ('cost_of_service',),
       ('data_origin',
        'origin_code',
        'entity',
       ),
       'user_comment',
       'comment_closing_status',
       'comment_intermediate_states',
     )
   }),
  )

  # readonly_fields = ('created_at','modified_at','user_id')

  def save_model(self, request, obj, form, change) -> None:

    obj.user_id = request.user.username
    return super().save_model(request, obj, form, change)
