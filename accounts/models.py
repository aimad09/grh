from django.db import models


# Create your models here.

class Departement(models.Model):
    nomDepart = models.CharField(max_length=100,null=True) 



class Service(models.Model):
    nomService = models.CharField(max_length=100,null=True) 


class Statut(models.Model):
     grade = models.CharField(max_length=100,null=True) 
     echelle= models.CharField(max_length=100,null=True) 
     salaireBase = models.IntegerField(null=True) 



class Fonction(models.Model):
    nomFonction = models.CharField(max_length=100,null=True) 


class Conge(models.Model):
    typeConge = models.CharField(max_length=100,null=True)
    quota = models.IntegerField(null=True)  



class Employe(models.Model):
    matricule = models.CharField(max_length=100,null=True)
    cin = models.CharField(max_length=100,null=True)
    nom = models.CharField(max_length=100,null=True)
    prenom = models.CharField(max_length=100,null=True)
    adresse = models.CharField(max_length=100,null=True)
    telephone = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    dateNaiss= models.DateField(null=True)
    dateRecrut= models.DateField(null=True)
    salaireBase = models.IntegerField(null=True)

    #defintion des clés étrangères
    Statut = models.ForeignKey('Statut', on_delete=models.SET_NULL,null=True )
    Fonction = models.ForeignKey('Fonction', on_delete=models.SET_NULL,null=True )
    Dept = models.ForeignKey('Departement', on_delete=models.SET_NULL,null=True )
    Service = models.ForeignKey('Service', on_delete=models.SET_NULL,null=True )



class demandeConge(models.Model):
    nbjourdemnade = models.IntegerField(null=True)
    employe = models.ForeignKey('Employe', on_delete=models.SET_NULL,null=True )
    typeconge = models.ForeignKey('Conge', on_delete=models.SET_NULL,null=True )


class validatConge(models.Model):
    date = models.DateField(null=True)
    etat = models.CharField(max_length=100,null=True)
    responsable = models.ForeignKey('Employe', on_delete=models.SET_NULL,null=True )
    demande = models.ForeignKey('demandeConge', on_delete=models.SET_NULL,null=True )

class authentification(models.Model):
    login = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    typecompte = models.CharField(max_length=100,null=True)
    employe = models.ForeignKey('Employe', on_delete=models.SET_NULL,null=True )

class demandeAbsence(models.Model):
    nbheure = models.IntegerField(null=True)
    period = models.CharField(max_length=100,null=True)
    employe = models.ForeignKey('Employe', on_delete=models.SET_NULL,null=True )

class validatAbsence(models.Model):
    etat = models.CharField(max_length=100,null=True)
    date = models.DateField(null=True)

    responsable = models.ForeignKey('Employe', on_delete=models.SET_NULL,null=True )
    demande = models.ForeignKey('validatAbsence', on_delete=models.SET_NULL,null=True )
