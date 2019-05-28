from django.urls import path
from . import views


urlpatterns = [
    path('login',views.loginpage, name= 'login'),
     path('admin',views.profile,name='profile'),
      path('register',views.register,name='register'),
   
]