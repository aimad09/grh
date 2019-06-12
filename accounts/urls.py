from django.urls import path
from . import views

urlpatterns = [
    path('login',views.loginpage, name= 'login'),
    path('admin',views.profile,name='profile'),
    path('register',views.register,name='register'),
    path('demande_conge',views.d_conge,name='demande_conge'),
    path('demande_absence',views.d_absence,name='demande_absence'),
    path('validation_conge',views.v_conge,name='validation_conge'),
    path('valider_conge',views.valider_conge,name='valider_conge'),
    
]