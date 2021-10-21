
#urls.py
from django.contrib import admin  
from django.urls import path  
from calculatorapp import views  
from django.conf.urls import url
from . import views
 
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('',views.index),
    path('history/',views.history,name='history'),

    
    url(r'^create$', views.create, name='create'),
]
