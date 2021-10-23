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

  description = models.CharField('descripción', max_length=100, unique=True)
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  # esta clase aplica para reenombrar los datos de la opción en el 
  # modelo para que aparezca en el adminPanel
  class Meta:
    verbose_name = 'categoria de servicio'
    verbose_name_plural = 'categoria de servicios'

  def __str__(self):
    return f'{self.description}'

class Entity(models.Model):
  description = models.CharField('nombre entidad', max_length=150, unique=True)
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
    verbose_name = 'sede administrativa'
    verbose_name_plural = 'sedes administrativas'

  def __str__(self) -> str:
      return f'{self.description}'

""" service models """
class Service(models.Model):

  category_service = models.ForeignKey(
    CategoryService, 
    on_delete=models.PROTECT, 
    verbose_name='categoría de servicio'
  )

  entity = models.ForeignKey(
    Entity, 
    on_delete=models.PROTECT, 
    null=True, 
    blank=True, 
    verbose_name='sede administrativa'
  )

  description = models.CharField('descripción', max_length=100,)
  web_indicator = models.BooleanField('indicador web', default=False)
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'servicio'
    verbose_name_plural = 'servicios'
    unique_together = [['description', 'category_service', 'entity']]
    

  def __str__(self) -> str:
      return f'{self.description}'

class Letter(models.Model):
  description = models.CharField('descripción', max_length=100, unique=True)
  letter_text = RichTextField(verbose_name="contenido")
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'Marco legal del servicio'
    verbose_name_plural = 'Marco legal de servicios'

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

  description = models.CharField('descripción', max_length=100, default=False)
  service = models.ForeignKey(Service, on_delete=models.PROTECT, verbose_name='servicio')
  letter = models.ForeignKey(Letter, on_delete=models.PROTECT, verbose_name='marco legal')
  order_display = models.IntegerField(
      'orden para mostrar',
      # null=False, 
      # blank=True,
      # choices=ORDER_DISPLAY,
      # default=''
  )
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'servicio y marco legal'
    verbose_name_plural = 'servicios y marco legal'
    unique_together = [['service', 'letter']]

  def __str__(self) -> str:
      return f'{self.service.description} {self.letter.description}'

class ComponentType(models.Model):
  
  description = models.CharField('nombre de componente', max_length=150, unique=True)
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'tipo de componente'
    verbose_name_plural = 'tipo de componentes'

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
  
  description = models.CharField('descripción', max_length=150, unique=True)

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
    unique_together = [['description', 'orientation','order_display']]

  def __str__(self) -> str:
    return f'{self.description}'

class MainSection(models.Model):
  description = models.CharField('descripción', max_length=250, unique=True)
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'sección principal de fomulario'
    verbose_name_plural = 'sección principal de formularios'
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

  def __str__(self) -> str:
      return f'{self.group_variable} - {self.description}'

class Subsection(models.Model):

  description = models.CharField('descripción', max_length=250, unique=True)
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  key_config = models.ForeignKey(
    ConfigVariable,
    on_delete=models.PROTECT, 
    verbose_name='key config', 
    null=True,
    blank=True,
    limit_choices_to={'group_variable': ('SECDF')}
  )

  class Meta:
    verbose_name = 'subsección de formulario'
    verbose_name_plural = 'subsección de formularios'
    db_table = 'request_subsection'

  def __str__(self) -> str:
    return f'{self.description}'  

class DataSource(models.Model):

  source = models.CharField('Fuente de datos', max_length=150, blank=False, unique=True)
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
    on_delete=models.PROTECT, 
    related_name="dataSourceValue"
  )
  
  code_data = models.CharField('código de lista de opciones', max_length=4, unique=True)
  value_data = models.CharField('descripción de lista de opciones', max_length=100)
  data_related = models.ForeignKey(
    'self',
    on_delete=models.PROTECT, 
    to_field='code_data',
    verbose_name='dato de fuente relacionada', 
    null=True,
    blank=True,
    # limit_choices_to={'data_related': (source_data)}
  )

  class Meta:
    verbose_name = 'valor de fuente de dato'
    verbose_name_plural = 'valores de fuentes de datos'
    db_table = 'request_data_source_value'
    unique_together = [['code_data', 'value_data', 'source_data']]
    

  def __str__(self) -> str:
    return f'{self.code_data} - {self.value_data}'

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

  population_filter_api = models.CharField(
    'filtro poblacional API', 
    null=True, 
    max_length=2000, 
    blank=True
  )

  start_date = models.DateField('fecha de inicio', null=True)
  end_date = models.DateField('fecha fin', null=True)
  delivery_days = models.IntegerField('días de entrega')
  bussiness_days = models.BooleanField('dias laborales', default=False)
  working_hours = models.BooleanField('horas laborales', default=False)
  is_active = models.BooleanField('activo', default=False)
  is_payment = models.BooleanField('requiere pago', default=False)
  is_form_active = models.BooleanField('formulario disponible', default=False)
  url_form = models.URLField('url formulario', max_length=500, null=True, blank=True)
  is_autenticado = models.BooleanField('requiere autenticación', default=False)
  valid_user = models.BooleanField('validación de usuario', default=False)
  
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

  # comments = RichTextField(
  #   verbose_name='comentarios del servicio', 
  # )
  comments = models.TextField('comentarios del servicio', null=True, blank=True)
  related_status = models.ManyToManyField(Status, through='ServiceConfigurationStatus')
  user_id = models.CharField('modificado por', max_length=50, blank=True)
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'regla de servicio'
    verbose_name_plural = 'reglas de servicios'
    db_table = 'request_service_configuration'

  def __str__(self) -> str:
    return f'{self.service_id}'

class MainFormSection(models.Model):

  # PRIMERO = '1'
  # SEGUNDO = '2'
  # TERCERO = '3'
  # CUARTO = '4'
  # QUINTO = '5'
  # ORDER_DISPLAY = [
  #     (PRIMERO, 'Primero'),
  #     (SEGUNDO, 'Segundo'),
  #     (TERCERO, 'Tercero'),
  #     (CUARTO, 'Cuarto'),
  #     (QUINTO, 'Quinto'),
  # ]
  
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

  order_display = models.IntegerField(
      'orden para mostrar', 
  )

  # user_id = models.CharField('modificado por', max_length=50, blank=True)
  # created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  # modified_at = models.DateTimeField('fecha de modicación', auto_now=True)

  class Meta:
    verbose_name = 'seccion principal de formularios'
    verbose_name_plural = 'sección principal de formularios'
    db_table = 'request_main_form_section'

  def __str__(self) -> str:
    return f'{self.rule_service}'

class subsectionServiceForm(models.Model):

  # PRIMERO = '1'
  # SEGUNDO = '2'
  # TERCERO = '3'
  # CUARTO = '4'
  # QUINTO = '5'
  # ORDER_DISPLAY = [
  #     (PRIMERO, 'Primero'),
  #     (SEGUNDO, 'Segundo'),
  #     (TERCERO, 'Tercero'),
  #     (CUARTO, 'Cuarto'),
  #     (QUINTO, 'Quinto'),
  # ]

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

  order_display = models.IntegerField(
      'orden para mostrar', 
  )

  class Meta:
    verbose_name = 'subsección de sección principal de formulario'
    verbose_name_plural = 'subsección de sección principal de formularios'
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

  # def get_key_head()->list:
  #   key_head_all = ConfigVariable.objects.filter(group_variable='HDSOL', system_required=True)
  #   key_body_all = ConfigVariable.objects.filter(group_variable='BDSOL')
  #   list_key_head = [(key_head_all[i].code, 'HEAD'+' - '+key_head_all[i].description) for i in range(len(key_head_all))]
  #   list_key_body = [(key_body_all[i].code, 'BODY'+' - '+key_body_all[i].description) for i in range(len(key_body_all))]
  #   list_all_key = list_key_head + list_key_body
  #   return sorted(list_all_key)

  key_config = models.ForeignKey(
    ConfigVariable,
    on_delete=models.PROTECT, 
    verbose_name='key config', 
    null=True,
    blank=True,
    limit_choices_to={'group_variable': ('HDSOL','BDSOL')}
  )

  # key_head = models.CharField(
  #   'key head',
  #   max_length=10,
  #   choices=get_key_head(),
  #   blank=True
  # )

  order_display = models.IntegerField('orden despliegue', null=True)
  
  class Meta:
    verbose_name = 'subsección y componente'
    verbose_name_plural = 'subsecciones y componentes'
    db_table = 'request_component_subsection'

  def __str__(self) -> str:
    return f'{self.description}'

class Priority(models.Model):
  description = models.CharField('description', max_length=255, unique=True)
  priority_percentage = models.FloatField('porcentaje de prioridad', default=0.0, unique=True)
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
    verbose_name='estado de solicitud',
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

class RequestHeader(models.Model):
  
  
  ORDER_DISPLAY = [
      ('1', 'Digital'),
      ('2', 'Físico'),
  ]
  id_usuario = models.CharField('identificador de usuario', max_length=60)
  email_applicant = models.EmailField('correo del solicitante', blank=True, null=True)
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

  term_code = models.CharField(
    'periodo solicictud', 
    max_length=12, 
    null=True, 
    blank=True
  )

  estimated_date = models.DateField(null=True)

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

  reception_date = models.DateField('fecha de recepción')
  delivery_date = models.DateField('fecha de entrega',)
  user_comment = models.TextField('comentario de usuario', null=True, blank=True)
  comment_closing_status = models.TextField('comentario para cierre del servicio', null=True, blank=True)
  comment_intermediate_states = models.TextField('comentario para estados intermedios', null=True, blank=True)
  data_origin = models.CharField('sistema origen de datos', max_length=60, default='SYSTEM INSTITUCIONAL')
  origin_code = models.CharField('código de origen', max_length=60, default='WEB')
  date_status_change = models.DateField('fecha de cambio de status')
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
    verbose_name_plural = 'gestión de solicitudes'
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




