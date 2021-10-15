""" requests models """
# from _typeshed import Self
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.db.models.base import Model
from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import PROTECT
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, User
from colorfield.fields import ColorField
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator

class Status(models.Model):

  code = models.CharField('código de estado', max_length=2, unique=True)
  description = models.CharField('descripción', max_length=150)
  completion_status = models.BooleanField('estado de terminación')
  visible_state = models.BooleanField('estado visible')
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'estado de solicitud'
    verbose_name_plural = 'estados de solicitudes'
    # db_table = 'request_status'

  def __str__(self) -> str:
    return f'{self.description}'

class CategoryService(models.Model):

  description = models.CharField('descripción', max_length=100)
  user_id = models.CharField('modificado por', max_length=50, blank=True)

  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  # esta clase aplica para reenombrar los datos de la opción en el 
  # modelo para que aparezca en el adminPanel
  class Meta:
    verbose_name = 'categoria de servicio'
    verbose_name_plural = 'categorias de servicios'

  def __str__(self):
    return f'{self.description}'

class Entity(models.Model):
  description = models.CharField('nombre entidad', max_length=150)
  email = models.EmailField('correo electrónico', max_length=200)
  root_entity = models.ForeignKey(
    'self', 
    on_delete=models.PROTECT, 
    verbose_name='entidad padre', 
    related_name='client_subordination',
    null=True,
    blank=True
  )
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'entidad'
    verbose_name_plural = 'entidades'

  def __str__(self) -> str:
      return f'{self.description}'

""" service models """
class Service(models.Model):

  category_service = models.ForeignKey(
    CategoryService, 
    on_delete=models.PROTECT, 
    verbose_name='categoria de servicio'
  )
  entity = models.ForeignKey(
    Entity, 
    on_delete=models.PROTECT, 
    null=True, 
    blank=True, 
    verbose_name='entidad prestadora'
  )
  description = models.CharField('descripción', max_length=100)
  web_indicator = models.BooleanField('indicador web', default=False)
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'servicio'
    verbose_name_plural = 'servicios'

  def __str__(self) -> str:
      return f'{self.description}'

class Letter(models.Model):
  description = models.CharField('descripción', max_length=100)
  letter_text = RichTextField(verbose_name="contenido")
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'Carta'
    verbose_name_plural = 'Cartas'

  def __str__(self) -> str:
      return f'{self.description}'

class LetterService(models.Model):

  PRIMERO = '1'
  SEGUNDO = '2'
  TERCERO = '3'
  CUARTO =  '4'
  QUINTO =  '5'
  ORDER_DISPLAY = [
      (PRIMERO, 'Primero'),
      (SEGUNDO, 'Segundo'),
      (TERCERO, 'Tercero'),
      (CUARTO,  'Cuarto'),
      (QUINTO,  'Quinto'),
  ]

  description = models.CharField('descripción', max_length=100, null=True, blank=True)
  service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='servicio')
  letter = models.ForeignKey(Letter, on_delete=models.CASCADE, verbose_name='carta')
  order_display = models.CharField(
      'orden para mostrar', 
      max_length=80, 
      # null=False, 
      # blank=True,
      choices=ORDER_DISPLAY,
      # default=''
  )
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'asociación de servicio y carta'
    verbose_name_plural = 'asociar servicios y cartas'

  def __str__(self) -> str:
      return f'{self.service.description} {self.letter.description}'

class ComponentType(models.Model):
  
  description = models.CharField('nombre de componente', max_length=150)
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'tipo de componente'
    verbose_name_plural = 'tipos de componentes'

  def __str__(self) -> str:
      return f'{self.description}'

class FooterWeb(models.Model):

  PRIMERO = '1'
  SEGUNDO = '2'
  TERCERO = '3'
  ORDER_DISPLAY = [
      (PRIMERO, 'Primero'),
      (SEGUNDO, 'Segundo'),
      (TERCERO, 'Tercero'),
  ]

  VERTICAL = 'V'
  HORIZONTAL = 'H'
  ORIENTATION = [
      (VERTICAL, 'Vertical'),
      (HORIZONTAL, 'Horizontal'),
  ]
  
  description = models.CharField('descripción', max_length=150)

  text_html = RichTextField(verbose_name='texto HTML')

  orientation = models.CharField(
    'orientación',
    max_length=1,
    choices=ORIENTATION
  )

  order_display = models.CharField(
      'orden para mostrar', 
      max_length=80, 
      choices=ORDER_DISPLAY,
  )

  is_active = models.BooleanField('activo', default=False)

  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'pie de pagina'
    verbose_name_plural = 'pies de paginas'
    db_table = 'request_footer_web'

  def __str__(self) -> str:
    return f'{self.description}'

class MainSection(models.Model):
  description = models.CharField('descripción', max_length=250)
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'sección principal'
    verbose_name_plural = 'secciones principales'
    db_table = 'request_main_section'

  def __str__(self) -> str:
    return f'{self.description}'

class ConfigVariable(models.Model):

  code = models.CharField('code', max_length=10)
  description = models.CharField('descripción', max_length=150)
  value = models.CharField('valor', max_length=20)
  sequence = models.IntegerField('secuencia', default=1)
  system_required = models.BooleanField('requerido por sistema', default=False)
  group_variable = models.CharField('grupo de variables', max_length=10)
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'variable de configuración'
    verbose_name_plural = 'variables de configuración'
    db_table = 'request_config_variable'
    unique_together = [['group_variable', 'code']]

  """ def __str__(self) -> str:
      return f'{self.description}'

  def hola(self) -> tuple:
    return (self.code, self.description)  """ 

class Subsection(models.Model):

  description = models.CharField('descripción', max_length=250)
  # key_config = models.CharField('key config', max_length=20, null=True)
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  def get_key_section_default()->list:
    try:
      key_head_section = ConfigVariable.objects.filter(code='HDSC', system_required=True)
    except:
      list_key_section = []
    
    list_key_section = [(key_head_section[i].code, key_head_section[i].description) for i in range(len(key_head_section))]
    return sorted(list_key_section)

  key_config = models.CharField(
    'key config',
    max_length=10,
    choices=get_key_section_default(),
    null=True,
    blank=True
  )

  class Meta:
    verbose_name = 'subsección'
    verbose_name_plural = 'subsecciones'
    db_table = 'request_subsection'

  def __str__(self) -> str:
    return f'{self.description}'  

class DataSource(models.Model):

  source = models.CharField('Fuente de datos', max_length=150, blank=False)
  related_source = models.ForeignKey(
    'self', 
    on_delete=models.PROTECT, 
    verbose_name='Fuente de datos relacionada', 
    related_name='source_related',
    null=True,
    blank=True
  )
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'fuente de datos'
    verbose_name_plural = 'fuentes de datos'
    db_table = 'request_data_source'

  def __str__(self) -> str:
    return f'{self.source}' 

class ConfigVariable(models.Model):

  code = models.CharField('código', max_length=10)
  description = models.CharField('descripción', max_length=150)
  value = models.CharField('valor', max_length=20)
  sequence = models.IntegerField('secuencia', default=1)
  system_required = models.BooleanField('requerido por sistema', default=False)
  group_variable = models.CharField('grupo de variables', max_length=10)
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'variable de configuración'
    verbose_name_plural = 'variables de configuración'
    db_table = 'request_config_variable'
    unique_together = [['group_variable', 'code']]

  """ def __str__(self) -> str:
      return f'{self.description}'

  def hola(self) -> tuple:
    return (self.code, self.description)  """ 

class CommunicationChannel(models.Model):

  code = models.CharField('código', max_length=10, unique=True)
  description = models.CharField('descripción', max_length=150)
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'canal de comunicación'
    verbose_name_plural = 'canales de comunicación'
    db_table = 'request_communication_channel'

  def __str__(self) -> str:
      return f'{self.description}'

class DataSourceValue(models.Model):

  source_data = models.ForeignKey(
    DataSource, 
    verbose_name='fuente de datos', 
    on_delete=models.CASCADE, 
    related_name="dataSourceValue"
  )

  # from_source_data = models.ForeignKey(
  #   DataSource, 
  #   on_delete=models.CASCADE, 
  #   related_name="from_dataSourceValue"
  # )
  
  code_data = models.CharField('código datos de la fuente', max_length=4)
  value_data = models.CharField('valor datos de la fuente', max_length=100)
  data_related = models.CharField('dato de fuente relacionada', max_length=4, null=True, blank=True)

  # order_display = models.CharField(
  #     'orden para mostrar', 
  #     max_length=80, 
  #     choices=ORDER_DISPLAY,
  # )
  # user_id = models.CharField('modificado por', max_length=50, blank=True)
  # created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  # modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'Valor de fuente de datos'
    verbose_name_plural = 'valores de fuentes de datos'
    db_table = 'request_data_source_value'

  def __str__(self) -> str:
    return f'{self.source_data}'

class ServiceConfiguration(models.Model):

  ORDER_DISPLAY = [
      ('1', 'Automático'),
      ('2', 'Semi-automático'),
      ('3', 'Manual'),
  ]
  
  service_id = models.ForeignKey(
    Service, 
    on_delete=models.PROTECT, 
    verbose_name='servicio'
  )
  role_id = models.ForeignKey(
    Group, 
    on_delete=models.PROTECT, 
    verbose_name='role de acceso', 
    null=True
  )
  population_filter_api = models.CharField('filtro poblacional API', null=True, max_length=2000, blank=True)
  start_date = models.DateField('fecha de inicio', null=True)
  end_date = models.DateField('fecha fin', null=True)
  delivery_days = models.IntegerField('dias de entrega', default=False)
  bussiness_days = models.BooleanField('dias laborales', default=False)
  working_hours = models.BooleanField('horas laborales', default=False)
  is_active = models.BooleanField('activo', default=False)
  is_payment = models.BooleanField('requiere pago', default=False)
  is_form_active = models.BooleanField('formulario activo', default=False)
  url_form = models.URLField('url formulario', max_length=500, null=True)
  is_autenticado = models.BooleanField('requiere autenticación', default=False)
  valid_user = models.BooleanField('validacion de usuario', default=False)
  
  generation_process = models.CharField(
    'Procesamiento',
    max_length=2,
    choices=ORDER_DISPLAY,
    null=True
  )

  cost_of_service = MoneyField (
    max_digits=14, 
    decimal_places=2, 
    default_currency='COP', 
    verbose_name='Costo del servicio',
    default=0,
    null=True
  )

  days_validity_document = models.IntegerField('dias de vigencia documento', default=0)
  digital_document = models.BooleanField('documento digital', default=False)
  physical_document = models.BooleanField('documento físico', default=False)

  comments = RichTextField(verbose_name='comentarios del servicio')
  related_status = models.ManyToManyField(Status, through='ServiceConfigurationStatus')
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'regla del servicio'
    verbose_name_plural = 'reglas del servicio'
    db_table = 'request_service_configuration'

  def __str__(self) -> str:
    return f'{self.service_id}'

class MainFormSection(models.Model):

  PRIMERO = '1'
  SEGUNDO = '2'
  TERCERO = '3'
  CUARTO = '4'
  QUINTO = '5'
  ORDER_DISPLAY = [
      (PRIMERO, 'Primero'),
      (SEGUNDO, 'Segundo'),
      (TERCERO, 'Tercero'),
      (CUARTO, 'Cuarto'),
      (QUINTO, 'Quinto'),
  ]
  
  rule_service = models.ForeignKey(
    ServiceConfiguration,
    verbose_name='Regla de servicio',
    on_delete=models.PROTECT,
    related_name="rules_service_main_form_section"
  )

  main_section = models.ForeignKey(
    MainSection,
    verbose_name='Sección principal formulario',
    on_delete=models.PROTECT,
    related_name='main_section_form',
    unique=True
  )

  is_active = models.BooleanField('activo', default=False)

  order_display = models.CharField(
      'orden para mostrar', 
      max_length=80, 
      choices=ORDER_DISPLAY,
  )

  # user_id = models.CharField('modificado por', max_length=50, blank=True)
  # created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  # modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'seccion principal y componentes form'
    verbose_name_plural = 'secciones principales y componentes form'
    db_table = 'request_main_form_section'

  def __str__(self) -> str:
    return f'{self.rule_service}'

class subsectionServiceForm(models.Model):

  PRIMERO = '1'
  SEGUNDO = '2'
  TERCERO = '3'
  CUARTO = '4'
  QUINTO = '5'
  ORDER_DISPLAY = [
      (PRIMERO, 'Primero'),
      (SEGUNDO, 'Segundo'),
      (TERCERO, 'Tercero'),
      (CUARTO, 'Cuarto'),
      (QUINTO, 'Quinto'),
  ]

  rule_service = models.ForeignKey(
    ServiceConfiguration,
    verbose_name='Regla de servicio',
    on_delete=models.PROTECT,
    related_name="rules_service_main_form_subsection"
  )

  subsection_service = models.ForeignKey(
    Subsection,
    verbose_name='subsección formulario',
    on_delete=models.PROTECT,
    related_name='subsection_form'
  )

  section_main_form = models.ForeignKey(
    MainSection,
    verbose_name='grupo principal del formulario',
    on_delete=models.PROTECT,
    null=True
  )

  is_active = models.BooleanField('activo', default=False)

  order_display = models.CharField(
      'orden para mostrar', 
      max_length=80, 
      choices=ORDER_DISPLAY,
  )

  class Meta:
    verbose_name = 'componente y seccion form'
    verbose_name_plural = 'componentes y secciones form'
    db_table = 'request_section_component'
    unique_together = [['rule_service','subsection_service', 'section_main_form']]

  def __str__(self) -> str:
    return f'{self.rule_service}'

class ComponentSubsection(models.Model):

  description = models.CharField('etiqueta del componente', max_length=255)

  rule_subsection = models.ForeignKey(
    subsectionServiceForm,
    verbose_name='Subsección de servicio',
    on_delete=models.PROTECT
  )

  component = models.ForeignKey(
      ComponentType,
      verbose_name='tipo de componente',
      on_delete=models.PROTECT
    )
  

  required = models.BooleanField('requerido', null=True) 

  source = models.ForeignKey(
    DataSource,
    verbose_name='fuente de datos',
    null=True,
    on_delete=models.PROTECT
  )

  source_api = models.CharField(
    'fuente de datos API',
    max_length=2000,
    null=True,
    blank=True
  )

  component_action = models.ForeignKey(
    'self',
    verbose_name='componente de acción',
    on_delete=models.PROTECT,
    null=True,
    blank=True
  )

  value_component_action = models.CharField(
    'valor componente acción',
    max_length=60,
    null=True,
    blank=True
  )

  def get_key_head()->list:
    key_head_all = ConfigVariable.objects.filter(group_variable='HDSOL', system_required=True)
    key_body_all = ConfigVariable.objects.filter(group_variable='BDSOL')
    list_key_head = [(key_head_all[i].code, 'HEAD'+' - '+key_head_all[i].description) for i in range(len(key_head_all))]
    list_key_body = [(key_body_all[i].code, 'BODY'+' - '+key_body_all[i].description) for i in range(len(key_body_all))]
    list_all_key = list_key_head + list_key_body
    return sorted(list_all_key)

  key_head = models.CharField(
    'key head',
    max_length=10,
    choices=get_key_head(),
    blank=True
  )

  order_display = models.IntegerField('orden despliegue', null=True)
  
  class Meta:
    verbose_name = 'subsección y componente'
    verbose_name_plural = 'subsecciones y componentes'
    db_table = 'request_component_subsection'

  def __str__(self) -> str:
    return f'{self.description}'

class ComponentMainForm(models.Model):

  rule_main_form = models.ForeignKey(
    MainFormSection,
    verbose_name='Subsección de servicio',
    on_delete=models.PROTECT
  ) 

  component = models.ForeignKey(
    ComponentType,
    verbose_name='componente',
    on_delete=models.PROTECT
  )

  description = models.CharField('etiqueta del componente', max_length=255)

  required = models.BooleanField('requerido', null=True) 

  source = models.ForeignKey(
    DataSource,
    verbose_name='fuente de datos',
    null=True,
    on_delete=models.PROTECT
  )

  source_api = models.CharField(
    'fuente de datos API',
    max_length=2000,
    null=True
  )

  def get_key_head()->list:
    key_head_all = ConfigVariable.objects.filter(group_variable='HDSOL', system_required=True)
    key_body_all = ConfigVariable.objects.filter(group_variable='BDSOL')
    list_key_head = [(key_head_all[i].code, 'HEAD'+' - '+key_head_all[i].description) for i in range(len(key_head_all))]
    list_key_body = [(key_body_all[i].code, 'BODY'+' - '+key_body_all[i].description) for i in range(len(key_body_all))]
    list_all_key = list_key_head + list_key_body
    return sorted(list_all_key)

  key_head = models.CharField(
    'key head',
    max_length=10,
    choices=get_key_head(),
    blank=''  
  )

  order_display = models.IntegerField('orden despliegue', null=True)

  
  class Meta:
    verbose_name = 'seccion principal y componente'
    verbose_name_plural = 'secciones principales y componentes'
    db_table = 'request_section_main_component'

  def __str__(self) -> str:
    return f'{self.rule_main_form}'

class Priority(models.Model):
  description = models.CharField('description', max_length=255)
  priority_percentage = models.FloatField('porcentaje de prioridad', default=0.0)
  color_priority = ColorField(default='#FF0000', verbose_name='Color de prioridad')
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'prioridad de servicio'
    verbose_name_plural = 'prioridades de servicios'
    db_table = 'request_priority'

  def __str__(self) -> str:
    return f'{self.description}'

class ServiceConfigurationStatus(models.Model):

  rule_service = models.ForeignKey(
    ServiceConfiguration,
    verbose_name='Servicio',
    on_delete=models.CASCADE
  )

  status_request = models.ForeignKey(
    Status,
    verbose_name='Estado de solicitud',
    on_delete=models.CASCADE
  ) 

  assign_to = models.ForeignKey(
    User,
    verbose_name='usuario asignado',
    on_delete=models.PROTECT,
    null=True
  )

  status_start = models.BooleanField('Estado de inicio')

  status_finished = models.BooleanField('estado de fin')

  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'estado relacionado a solicitud'
    verbose_name_plural = 'estados relacionados a solicitudes'
    db_table = 'request_status_related_request'

  def __str__(self) -> str:
    return f'{self.rule_service}'

class ComponentAction(models.Model):

  service_id = models.ForeignKey(
    ServiceConfiguration, 
    verbose_name='Servicio',
    on_delete=models.PROTECT
  )

  service_component_group_id = models.ForeignKey(
    MainSection, 
    verbose_name='grupo de componentes', 
    null=True,
    on_delete=models.PROTECT
  )

  service_component_section_id = models.ForeignKey(
    Subsection,
    verbose_name='seccion de formularios',
    null=True,
    on_delete=models.PROTECT,
  )
  
  # user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'componente de acción formularios'
    verbose_name_plural = 'componentes de acción formularios'
    db_table = 'request_component_action'
    unique_together = [['service_id', 'service_component_group_id', 'service_component_section_id']]

  def __str__(self) -> str:
    return f'{self.service_id}'

class RequestHeader(models.Model):
  
  
  ORDER_DISPLAY = [
      ('1', 'Digital'),
      ('2', 'Físico'),
  ]
  id_usuario = models.CharField('identificador de usuario', max_length=60)
  rule_service = models.ForeignKey(
    ServiceConfiguration,
    verbose_name='servicio configurado',
    on_delete=models.PROTECT
  )

  service = models.ForeignKey(
    Service,
    verbose_name='servicio',
    on_delete=models.PROTECT
  )

  status_service = models.ForeignKey(
    Status,
    verbose_name='status del servicio',
    on_delete=PROTECT
  )

  term_code = models.CharField('periodo solicictud', max_length=12)

  estimated_date = models.DateTimeField(null=True)

  document_type = models.CharField(
      'tipo de documento', 
      max_length=1, 
      choices=ORDER_DISPLAY,
      default=1
  )

  communication_channel = models.ForeignKey(
    CommunicationChannel,
    verbose_name='Canal de comunicación',
    on_delete=models.PROTECT,
    null=True
  )

  correspondence_address = models.CharField(max_length=400, null=True)

  copies = models.IntegerField('numero de copias')

  cost_of_service = MoneyField (
    max_digits=14, 
    decimal_places=2, 
    default_currency='COP', 
    verbose_name='Costo del servicio',
    default=0,
    null=True
  )

  reception_date = models.DateTimeField('fecha de recepción', auto_now_add=True)
  delivery_date = models.DateTimeField('fecha de entrega',)
  user_comment = models.TextField('comentario de usuario',)
  comment_closing_status = models.TextField('comentario para cierre del servicio')
  comment_intermediate_states = models.TextField('comentario para estados intermedios')
  data_origin = models.CharField('sistema origen de datos', max_length=60, default='SYSTEM INSTITUCIONAL')
  origin_code = models.CharField('código de origen', max_length=60, default='WEB')
  date_status_change = models.DateTimeField('fecha de cambio de status')
  entity = models.ForeignKey(
    Entity,
    verbose_name='campus',
    on_delete=models.PROTECT
  )

  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'gestión de la solicitud'
    verbose_name_plural = 'gestión de las solicitudes'
    db_table = 'request_header'
    # unique_together = [['service_id', 'service_component_group_id', 'service_component_section_id']]

  def __str__(self) -> str:
    return f'{self.rule_service}'

class RequestBody(models.Model):

  header_request_id = models.ForeignKey(
    RequestHeader,
    verbose_name='codigo solicitud',
    on_delete=models.PROTECT
  )

  component_service_id = models.ForeignKey(
    ComponentSubsection,
    verbose_name='componente de formulario',
    on_delete=models.CASCADE
  )

  data_code = models.CharField('código de pregunta', max_length=10)
  data_desc = models.CharField('selección de respuesta', max_length=255)

  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'cuerpo de la solicitud'
    verbose_name_plural = 'cuerpo de las solicitudes'
    db_table = 'request_body'
    # unique_together = [['service_id', 'service_component_group_id', 'service_component_section_id']]

  def __str__(self) -> str:
    return f'{self.header_request_id}'

class RequestHistory(models.Model):
  
  
  ORDER_DISPLAY = [
      ('1', 'Digital'),
      ('2', 'Físico'),
  ]

  header_request_id = models.ForeignKey(
    RequestHeader,
    verbose_name='codigo solicitud',
    on_delete=models.PROTECT,
    null=True
  )

  id_usuario = models.CharField('identificador de usuario', max_length=60)
  rule_service = models.ForeignKey(
    ServiceConfiguration,
    verbose_name='servicio configurado',
    on_delete=models.PROTECT
  )

  service = models.ForeignKey(
    Service,
    verbose_name='servicio',
    on_delete=models.PROTECT
  )

  status_service = models.ForeignKey(
    Status,
    verbose_name='status del servicio',
    on_delete=PROTECT
  )

  term_code = models.CharField('periodo solicictud', max_length=12)

  estimated_date = models.DateTimeField(null=True)

  document_type = models.CharField(
      'tipo de documento', 
      max_length=1, 
      choices=ORDER_DISPLAY,
      default=1
  )

  communication_channel = models.ForeignKey(
    CommunicationChannel,
    verbose_name='Canal de comunicación',
    on_delete=models.PROTECT,
    null=True
  )

  correspondence_address = models.CharField(max_length=400, null=True)

  copies = models.IntegerField('numero de copias')

  cost_of_service = MoneyField (
    max_digits=14, 
    decimal_places=2, 
    default_currency='COP', 
    verbose_name='Costo del servicio',
    default=0,
    null=True
  )

  reception_date = models.DateTimeField('fecha de recepción', auto_now_add=True)
  delivery_date = models.DateTimeField('fecha de entrega',)
  user_comment = models.TextField('comentario de usuario',)
  comment_closing_status = models.TextField('comentario para cierre del servicio')
  comment_intermediate_states = models.TextField('comentario para estados intermedios')
  date_status = models.DateTimeField('fecha de cambio de status')
  comment_change_type = models.CharField('comentario del cambio', max_length=255)

  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'historia de la solicitud'
    verbose_name_plural = 'historia de solicitudes'
    db_table = 'request_history'
    # unique_together = [['service_id', 'service_component_group_id', 'service_component_section_id']]

  def __str__(self) -> str:
    return f'{self.rule_service}'




