from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.elastic_helper import e_search
# Create your views here.
response_format ={}
def Responsedata(message,code,data):
	response_format['code'] = code
	response_format['message'] = message
	response_format['data'] = data
	return response_format

def index(request):
	return HttpResponse("Elastic Service")


def e_search_view(request,keyword):
	try:
		print(keyword)
		data  = e_search(keyword)
		return JsonResponse(Responsedata("",0,data))
	except Exception as e:
		print(e)
		return JsonResponse(Responsedata("",0,"error"))