from django.urls import path
from .views import SignUpView
from users import views  

urlpatterns = [
path('signup/', SignUpView.as_view(), name='signup'),
path('history/', views.history),
]