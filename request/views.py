from request.models import CategoryService
from django.shortcuts import render
from django.http import JsonResponse

class JSONResponseMixin:

  def render_to_json_response(self, context, **response_kwargs):

    return JsonResponse(
      self.get_data(context),
      **response_kwargs,
    )

  def get_data(self, context):
    category = CategoryService .objects.all(('id','description',),)

    return(JsonResponse(category))