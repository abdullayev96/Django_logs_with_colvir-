from django.urls import path
from .views import *


urlpatterns = [
    path('', Index, name="index"),
    path('login/', Login_page, name='login'),
    path('logout/', LogoutView, name='logout'),
    
]