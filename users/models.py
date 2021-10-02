""" Users Models. """

# Django
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
  """ Pofile Models
      
      Proxy model that extends the base data with other information
  """

  user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
  website = models.URLField("sitio Web", max_length=250, blank=True)
  biography = models.TextField('biografía',blank=True)
  phone_number = models.CharField('número telefónico',max_length=20, blank=True)
  picture = models.ImageField(
    'Imagen de perfil',
    upload_to = 'users/picture',
    blank=True,
    null = True
  )
  created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
  modified_at = models.DateTimeField('fecha de modificación', auto_now=True)

  class Meta:
    verbose_name = 'perfil'
    verbose_name_plural = 'perfiles'

  def __str__(self):
    """ retrun name """
    return self.user.username





