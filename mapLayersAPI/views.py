from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
# import json
# from mapLayersAPI.models import MunicipalService
# from django.views.generic import View
#
# class ResponseApie(View):
#     def get(self,request):
#         obj = MunicipalService.objects.all()
#         output={}
#         for obje in obj:
#             rr = {'name':obje.service, 'id':obje.service_id}
#             # if
#             if obje.category not in output.keys():
#                 output[obje.category]=[]
#                 output[obje.category].append({'name':obje.service, 'id':obje.service_id})
#             else:
#                 if rr not in output[obje.category]:
#                     output[obje.category].append({'name':obje.service, 'id':obje.service_id})
#         return HttpResponse(json.dumps(output), content_type='application/json')
