from django.views.generic import TemplateView
from django.shortcuts import render
from django_ajax.decorators import ajax
import requests
import json
from django.http import HttpResponse
import sqlite3
from django.template import RequestContext
#from django.http import HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie

class HomeView(TemplateView):  
    template_name = 'home/home.html'

    def getData():
        r = requests.get("https://jsonplaceholder.typicode.com/users", verify=False)
       
        return HttpResponse(r)
        
    def addData(request):
        response = {
           "status":"Success"
        }
        return JsonResponse(response)

def getData():
        r = requests.get("https://jsonplaceholder.typicode.com/users", verify=False)
       
        return HttpResponse(r)
        
def addData(request):
    '''
    1.add data from webapi
    '''
    
    response = requests.get("https://jsonplaceholder.typicode.com/users", verify=False)
   
    ls=response.json()
    
    conn = sqlite3.connect(r'D:\Tutor\Django\testPassValue\testPassValue\testPassValue.db')
    cursor = conn.cursor()
    execution = "delete from users"
    cursor.execute(execution)
    conn.commit()
    
    conn = sqlite3.connect(r'D:\Tutor\Django\testPassValue\testPassValue\testPassValue.db')
    cursor = conn.cursor()
        
    for i in range(10):
        execution = "INSERT INTO users(id, name, username, email, address_street, address_suite, address_city,address_zipcode, geo_lat, geo_lng, phone, website, company_name, company_catchPhrase,company_bs  ) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}')".format(ls[i]["id"], ls[i]["name"], ls[i]["username"], ls[i]["email"], ls[i]["address"]["street"], ls[i]["address"]["suite"], ls[i]["address"]["city"], ls[i]["address"]["zipcode"], ls[i]["address"]["geo"]["lat"], ls[i]["address"]["geo"]["lng"], ls[i]["phone"],ls[i]["website"],ls[i]["company"]["name"],ls[i]["company"]["catchPhrase"],ls[i]["company"]["bs"] )
        cursor.execute(execution)
        conn.commit()
        
    
    conn.close()
    
    response = {
       "status":"Success"
    }
    return HttpResponse(response)

def post(request):
    '''
    2.add user & catchPhrase from webpage
    '''
    
    #if request.is_ajax():
    #    userName = request.POST.get('userName', None)           # getting data from userName input 
    #    catchPhrase = request.POST.get('catchPhrase', None)     # getting data from catchPhrase input
        
    conn = sqlite3.connect(r'D:\Tutor\Django\testPassValue\testPassValue\testPassValue.db')
        
    cursor = conn.cursor()
    cursor.execute('SELECT max(id)+1 as id FROM users')
    row = cursor.fetchone()    

    id = int(row[0])
        
    execution = "INSERT INTO users(id, username, company_catchPhrase ) VALUES ({0}, '{1}', '{2}')".format(id, 'ralphchen','pass' )
    cursor.execute(execution)
    conn.commit()

    conn.close()
    
    response = {
       "status":"Success"
    }
    return HttpResponse(response)

    
def checkUsers(request):
    '''
    3.1. checkUsers
    '''
    ls=[]
    dict = {};
    
    conn = sqlite3.connect(r'D:\Tutor\Django\testPassValue\testPassValue\testPassValue.db')
        
    cursor = conn.cursor()
    cursor.execute('SELECT id,company_catchPhrase FROM users')
    row = cursor.fetchone()    

    while row:
        dict[str(int(row[0]) - 1)] = str(row[1])
        row = cursor.fetchone()
    
    ls.append(dict)
        
    conn.close()
    
    return HttpResponse(ls)
    
def getUsers(request):
    '''
    3.2. getUsers
    '''
    ls=[]
    dict = {};
    
    conn = sqlite3.connect(r'D:\Tutor\Django\testPassValue\testPassValue\testPassValue.db')
        
    cursor = conn.cursor()
    cursor.execute('SELECT id,company_catchPhrase FROM users')
    row = cursor.fetchone()    

    while row:
        dict[str(int(row[0]) - 1)] = str(row[1])
        row = cursor.fetchone()
    
    ls.append(dict)
        
    conn.close()
    
    return HttpResponse(ls)
    