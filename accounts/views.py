from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .form import LoginForm
from .models import authentification
from .models import Employe


# Create your views here.

def authenticate(username,password):
   for auth in authentification.objects.all():
            if username == auth.login and password == auth.password :
               return auth.typecompte
   return None       

def loginpage(request):
   if request.method =='POST':
      #form = LoginForm(request.POST)

     # if form.is_valid():
        # username = form.cleaned_data.get('usern')
         #pwd = form.cleaned_data.get('pwd')
         username = request.POST.get('username')
         pwd = request.POST.get('password')
         auth = authenticate(username,pwd)
         if auth != None :
               request.session['login'] = username
               request.session['password'] = pwd
               request.session['compte'] = auth
               link = 'accounts/'+auth+'.html'
               return render(request,link,locals())
         
  # else:
     # form = LoginForm()
   return render(request,'accounts/login1.html',locals())




def profile(request):
   return render(request,'accounts/admin.html')


def register(request):
   exist = False
   typecompte=""
   if request.method =='POST':
      cin= request.POST.get('cin')
      registNumber = request.POST.get('registnumb')
      username = request.POST.get('username')
      pwd = request.POST.get('password')
      pwd1 = request.POST.get('password1')  
      for emp in Employe.objects.all():
            if cin == emp.cin and  registNumber== emp.matricule :
               exist = True
               if emp.Fonction_id == 1:
                  typecompte = "admin"
               elif emp.Fonction_id ==2 or emp.Fonction_id ==3 :
                    typecompte = "responsable"
               else:
                   typecompte = "employe"
               if pwd == pwd1 :
                  auth = authentification(login = username,password = pwd ,typecompte = typecompte )
                  auth.save()
   return render(request,'accounts/register.html',locals())

