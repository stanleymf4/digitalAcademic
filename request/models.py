""" requests models """
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

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
    on_delete=models.CASCADE, 
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

  category_service = models.ForeignKey(CategoryService, on_delete=models.CASCADE, verbose_name='categoria de servicio')
  entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True, verbose_name='entidad prestadora')
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
      null=False, 
      blank=True,
      choices=ORDER_DISPLAY,
      default=''
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



