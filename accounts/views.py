from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from datetime import datetime, time, tzinfo, timedelta
from .form import LoginForm,DateForm
from .models import authentification
from .models import Employe
from .models import demandeConge,Conge,demandeAbsence,validatConge
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
               request.session['login'] = username
               request.session['password'] = pwd
               request.session['compte'] = auth.typecompte
               link = 'accounts/'+auth.typecompte+'.html'
               return render(request,link,locals())
         
  # else:
     # form = LoginForm()
   return render(request,'accounts/login1.html',locals())




def profile(request):
   return render(request,'accounts/admin.html')


def register(request):
   message = {}
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

#demande de congé
def d_conge(request):
   if request.method == 'POST':
      nbrjour=0
      c=0
      date_debut = request.POST['date'] 
      nbrjour = request.POST['nbrjour']
      t_conge = request.POST['type_conge']
      emp = Employe.objects.get(id=1)
      cong = Conge.objects.get(id= emp.typeconge_id)
      c=cong.quota-int(nbrjour)
      conge = Conge(
         typeConge = t_conge,
         quota = c
      )
      conge.save()
      demande =  demandeConge(
            datedebut = date_debut ,
            nbjourdemnade = nbrjour,
            #typeconge=conge
      )
      demande.typeconge=conge
      demande.save()
      valconge = validatConge(demande = demande)
      
      valconge.save()
   else:
      error=1
   return render(request,'accounts/demande_conge.html',locals())

def d_absence(request):
   if request.method == 'POST':  
      heurs_absence = datetime.now()
      heurs_absence = request.POST['h_absence']
      periode = request.POST['periode']
      nbr_heurs = request.POST['nbr_heurs']
      
      demande = demandeAbsence(
         
         heurabsence = heurs_absence,
         nbheure = nbr_heurs,
         period = periode 
      )
      demande.save()
   else:
      error=1
   return render(request,'accounts/demande_absence.html',locals())

def v_conge(request):

   valconge =  validatConge.objects.all()
   return render(request,'accounts/validation_conge.html',locals())

def valider_conge(request):
   if request.method == 'POST':
      demand_id = request.POST['demand_id']
      etat= request.POST['etat']
      date = datetime.now()
      
      validerconge = validatConge(
         date=date,
         etat=etat,
      )
      
      validerconge.demande=demandeConge.objects.get(id=demand_id)
      validerconge.save()
      data = {}
      data['validate'] = model_to_dict(validerconge)
   
   return JsonResponse(data)
      
