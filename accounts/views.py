from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,JsonResponse 
from datetime import datetime
from .form import LoginForm
from .models import authentification
from .models import Employe,Service,Fonction,Departement
from django.core import serializers
import json
from django.forms.models import model_to_dict

# Create your views here.

def authenticate(username,password):
   for auth in authentification.objects.all():
            if username == auth.login and password == auth.password :
               return auth
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
               request.session['auth'] = auth
               return redirect(profile)
         
  # else:
     # form = LoginForm()
   return render(request,'accounts/login1.html',locals())




def profile(request):
   
   auth = request.session['auth'] 
   employes = Employe.objects.all()
   services = Service.objects.all()
   depart = Departement.objects.all()
   fonctions = Fonction.objects.all()
   link = 'accounts/'+auth.typecompte+'.html'
   return render(request,link,locals())


def register(request):
   message = ""
   typecompte=""
   if request.method =='POST':
      cin= request.POST.get('cin')
      registNumber = request.POST.get('registnumb')
      username = request.POST.get('username')
      pwd = request.POST.get('password')
      pwd1 = request.POST.get('password1')  
      for emp in Employe.objects.all():
            if cin == emp.cin and  registNumber== emp.matricule :
               if emp.Fonction_id == 1:
                  typecompte = "admin"
               elif emp.Fonction_id ==2 or emp.Fonction_id ==3 :
                    typecompte = "responsable"
               else:
                   typecompte = "employe"
               if pwd == pwd1 :
                  if fetch_auth(emp.id) == None   :
                    
                     auth = authentification(login = username,password = pwd ,typecompte = typecompte,employe_id=emp.id )
                     auth.save()
                     message ="success"
                    
                  else:
                      message =  "danger"
               else:
                    message =  "info"   
            else :
               message = "warning"
              
   return render(request,'accounts/register.html',locals())


def fetch_auth(id) :
   for auth in authentification.objects.all():
            if  auth.employe_id == id :
            	return auth
   return None       


def fetch(request):
   if request.method == 'POST':
      employes = Employe.objects.all()
      services = Service.objects.all()
      depart = Departement.objects.all()
      fonctions = Fonction.objects.all()
      data = {}
       
      
      #employes =  serializers.serialize('json', employes)
      '''
      data["services"] =  serializers.serialize('json',services)
      data["depart"] =  serializers.serialize('json',depart)
      data["fonctions"] =  serializers.serialize('json', fonctions)
      '''
     
   return employes

def createEmployee(request):
   if request.method == 'POST':
      matricule = request.POST.get('matricule')
      cin = request.POST.get('cin')
      firstname = request.POST.get('firstname')
      lastname = request.POST.get('lastname')
      adresse = request.POST.get('adresse')
      teleph = request.POST.get('teleph')
      email = request.POST.get('email')
      birthdate = request.POST.get('birthdate')
      startdate = request.POST.get('startdate')
      salaire = request.POST.get('salaire')
      fonction =  request.POST.get('position')
      service =  request.POST.get('service')
      depart =  request.POST.get('depart')

      emp = Employe(matricule = matricule,cin =cin,nom =lastname,prenom=firstname,adresse=adresse,
      telephone=teleph,email=email,dateNaiss = birthdate,dateRecrut=startdate,salaireBase=int(salaire),
      Service_id = int(service),Fonction_id=int(fonction),Dept_id=int(depart) )
      emp.save()
      data = {}
      data['emp'] = model_to_dict(emp)
     
   return JsonResponse(data)







def fetch_single(request):
   if request.method == 'POST':
      empid = request.POST.get('empid')
      emp = Employe.objects.filter(id=empid).first()
      print(emp.Fonction_id)
      data = {}
      data['emp'] = model_to_dict(emp)
   return JsonResponse(data)