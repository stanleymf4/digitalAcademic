from django.http.response import HttpResponse
from request.models import CategoryService, ComponentSubsection, MainFormSection, MainSection, Subsection, subsectionServiceForm
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

def get_data_group(request):
  if request.GET['service_id'] != '':
    main_section_form = MainFormSection.objects.filter(rule_service_id=request.GET['service_id'])
    list_main_section_form = [e.main_section_id for e in main_section_form]
    main_section = serializers.serialize(
      "json", 
      MainSection.objects.filter(
        id__in = list_main_section_form
      ).only(
        'id',
        'description'
      )
    )
  else:
    main_section_genral = MainSection.objects.all()
    main_section = serializers.serialize(
      "json", 
      main_section_genral.only(
        'id',
        'description'
      )
    )
  
  return JsonResponse(main_section, safe=False)

def get_data_section(request):
  if request.GET['service_component_group_id'] != '':
    section_form = subsectionServiceForm.objects.filter(section_main_form=request.GET['service_component_group_id'])
    list_section_form = [e.subsection_service_id for e in section_form]
    print(list_section_form)
    sections = serializers.serialize(
      "json", 
      Subsection.objects.filter(
        id__in = list_section_form
      ).only(
        'id',
        'description'
      )
    )
  else:
    section_genral = Subsection.objects.all()
    sections = serializers.serialize(
      "json", 
      section_genral.only(
        'id',
        'description'
      )
    )
  
  return JsonResponse(sections, safe=False) 

