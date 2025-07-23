from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home_view(request):
   name="sreekar"
   return render(request,'home.html',{'name':name})

def food(request):
   return render(request,'food.html')
'''
def testu_view(request):
   return render(request,'home/testu.html')

def contact(request):
   name=request.GET.get('name')
   return render(request,'home/home.html',{'name':name})
'''
def name(request,name):
   #name=request.GET.get('name')
   return render(request,'home/home.html',{'name':name})

def http_resp(request):
   return HttpResponse('<h1>welcome back mr.ashura</h1>')

def json_data(request):
   data={'name':'sreekaru'}
   return JsonResponse(data)