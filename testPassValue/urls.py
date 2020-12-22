from django.conf.urls import url, include
from testPassValue.views import HomeView,addData
#from django.contrib import admin
from django.urls import path
from testPassValue import views

urlpatterns = [  
  url(r'^$', HomeView.as_view(), name="home"),
  #url(r'^getData/$', getData, name='getData'),
  #url(r'^testPassValue/$', views.addData, name='addData'),
  #url(r'^testPassValue/', include('testPassValue.urls')),
  #url(r'^addData/$', HomeView.addData),
  #path('add_Data', addData, name="Add_Data"),
  url(r'^addData/$', views.addData, name='addData'),
]