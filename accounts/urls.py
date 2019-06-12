from django.urls import path
from . import views


urlpatterns = [
    path('/login',views.loginpage, name= 'login'),
    path('/admin',views.profile,name='profile'),
    path('/register',views.register,name='register'),
    path('/createEmployee',views.createEmployee,name='createEmployee'),
    path('/fetch',views.fetch,name='fetch'),
    path('/fetch_single',views.fetch_single,name='fetch_single'),
   
]