from django.views.generic import TemplateView
from django.shortcuts import render
from django_ajax.decorators import ajax
import requests
import json
from django.http import HttpResponse
import sqlite3

class HomeView(TemplateView):  
    template_name = 'home/home.html'

    #@ajax
    def getData():
        r = requests.get("https://jsonplaceholder.typicode.com/users", verify=False)
       
        return HttpResponse(r)
      
      
    ##def addData(request):
    ##    return render(request,'./home//home.html')
        
    def addData(request):
        response = {
           "status":"Success"
        }
        return JsonResponse(response)

def getData():
        r = requests.get("https://jsonplaceholder.typicode.com/users", verify=False)
       
        return HttpResponse(r)
        
def addData(request):
    #response = {
    #   "status":"Success"
    #}
    #return HttpResponse(response)
    
    response = requests.get("https://jsonplaceholder.typicode.com/users", verify=False)
   
    ls=response.json()
    #data2 = json.dumps(ls, sort_keys=True, indent=4, separators=(',', ': '))
    
    conn = sqlite3.connect(r'D:\Tutor\Django\testPassValue\testPassValue\testPassValue.db')
    cursor = conn.cursor()
    execution = "delete from users"
    cursor.execute(execution)
    conn.commit()
    
    #execution = "INSERT INTO users(id, name, username, email, address_street, address_suite, address_city,address_zipcode, geo_lat, geo_lng, phone, website, company_name, company_catchPhrase,company_bs  ) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}')".format(ls[0]["id"], ls[0]["name"], ls[0]["username"], ls[0]["email"], ls[0]["address"]["street"], ls[0]["address"]["suite"], ls[0]["address"]["city"], ls[0]["address"]["zipcode"], ls[0]["address"]["geo"]["lat"], ls[0]["address"]["geo"]["lng"], ls[0]["phone"],ls[0]["website"],ls[0]["company"]["name"],ls[0]["company"]["catchPhrase"],ls[0]["company"]["bs"] )
    #cursor.execute(execution)
    #execution = "INSERT INTO users(id, name, username ) VALUES ('{0}', '{1}', '{2}')".format(ls[1]["id"], ls[1]["name"], ls[1]["username"] )
    #cursor.execute(execution)
    #execution = "INSERT INTO users(id, name, username ) VALUES ('{0}', '{1}', '{2}')".format(ls[2]["id"], ls[2]["name"], ls[2]["username"] )
    #cursor.execute(execution)
    #conn.commit()
    #conn.close()
    
    conn = sqlite3.connect(r'D:\Tutor\Django\testPassValue\testPassValue\testPassValue.db')
    cursor = conn.cursor()
        
    for i in range(10):
        #id=ls[i]["id"]
        #name=ls[i]["name"]
        #username=ls[i]["username"]
        #email=ls[i]["email"]
        #address_street=ls[i]["address"]["street"]
        #address_suite=ls[i]["address"]["suite"]
        #address_city=ls[i]["address"]["city"]
        #address_zipcode=ls[i]["address"]["zipcode"]
        #geo_lat=ls[i]["geo"]["lat"]
        #geo_lng=ls[i]["geo"]["lng"]
        #phone=ls[i]["phone"]
        #website=ls[i]["website"]
        #company_name=ls[i]["company"]["name"]
        #company_catchPhrase=ls[i]["company"]["catchPhrase"]
        #company_bs=ls[i]["company"]["bs"]
        
        
        #execution = "INSERT INTO users(id, name, username, email, address_street, address_suite, address_city,address_zipcode, geo_lat, geo_lng, phone, website, company_name, company_catchPhrase,company_bs ) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', {5}, '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}')".format(id, name, username, email, address_street, address_suite, address_city, address_zipcode,geo_lat, geo_lng, phone,website, company_name, company_catchPhrase,company_bs )
        #execution = "INSERT INTO users(id, name, username ) VALUES ('{0}', '{1}', '{2}')".format(ls[i]["id"], ls[i]["name"], ls[i]["username"] )
        execution = "INSERT INTO users(id, name, username, email, address_street, address_suite, address_city,address_zipcode, geo_lat, geo_lng, phone, website, company_name, company_catchPhrase,company_bs  ) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}')".format(ls[i]["id"], ls[i]["name"], ls[i]["username"], ls[i]["email"], ls[i]["address"]["street"], ls[i]["address"]["suite"], ls[i]["address"]["city"], ls[i]["address"]["zipcode"], ls[i]["address"]["geo"]["lat"], ls[i]["address"]["geo"]["lng"], ls[i]["phone"],ls[i]["website"],ls[i]["company"]["name"],ls[i]["company"]["catchPhrase"],ls[i]["company"]["bs"] )
        cursor.execute(execution)
        conn.commit()
        
    
    conn.close()
    
    #return HttpResponse(ls[0]["name"])
    #return HttpResponse(address_street)
    
    response = {
       "status":"Success"
    }
    return HttpResponse(response)
    