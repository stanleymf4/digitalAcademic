from datetime import datetime

category_services = [
  {
    'description': 'ACADEMICA',
    'user_mod': 'stanley'
  },
  {
    'description': 'ADMINISTRATIVAS',
    'user_mod': 'stanley'
  },
  {
    'description': 'FINANCIERA',
    'user_mod': 'stanley'
  }
]

from request.models import CategoryService

for category in category_services:
  obj = CategoryService(**category)
  obj.save()
  print(obj.pk, ':', obj.description)