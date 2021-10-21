from django.contrib import admin
from django.urls import path, include # new
from users import views  
from django.conf.urls import url
from django.views.generic.base import TemplateView # new
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', include('calculatorapp.urls')), 
    
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')), # new
    path('users/', include('django.contrib.auth.urls')), # new
    path('', TemplateView.as_view(template_name='home.html'),name='home'),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('password/',auth_views.PasswordChangeView.as_view()),
 
    
   ]
