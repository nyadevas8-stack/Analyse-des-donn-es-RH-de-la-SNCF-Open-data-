# # -*- coding: utf-8 -*-
# """
# Created on Mon Jan  6 13:53:12 2025

# @author: Nya Devas
# """
# import csv
# """Fonctions"""

# def importer(fichier) :
#     """
#     charge le ficihier csv

#     Parameters
#     ----------
#     fichier : string
#       fichier a importer 

#     Returns
#     -------
#    string
#        return une liste du fichier csv 
#     """
#     with open(fichier,"r") as fich :
#         data=csv.reader(fich,delimiter=";",lineterminator="\n")
#         return list(data)
    
    
# def afficher(liste) :
#     """
#    affiche les informations des fichiers tabulaires sur 15 caractéres

#     Parameters
#     ----------
#     liste : string
#        la liste obetenue avec le fichier csv 

#     Returns
#     -------
#     None.

#     """
#     for ligne in liste :
#        print(f"{ligne[0]:<6} {ligne[1]:40} {ligne[2]:15} {ligne[3]:8} {ligne[4]:<6}")
#     print()
    

# def renommer_variables(datalist) :
#     """
#     renommer des variables lorsqu'elle ne respecte pas le format de variable'

#     Parameters
#     ----------
#     datalist : list of list
#         DESCRIPTION.

#     Returns
#     -------
#     None.

#     """
    
#     for i in range (len(datalist[0])) :
#           print(f"variable{i}={datalist[0][i]}")
#           nouveau=input("entrer le nouveau nom (sinon valider ) : ")
#           if nouveau:
#              datalist[0][i]=nouveau
        
      
# def Index_variable(datalist,variable) :
#     """
#     affiche l'index d'une variable donner

#     Parameters
#     ----------
#     datalist : list of list
#         DESCRIPTION.
#     variable :string
#        nom de la variable
#     Returns
#     -------
#     None.

#     """
    
#     i=datalist[0].index(variable)
#     return i
       

# def exporter(datalist,fichier) :
#     """
    

#     Parameters
#     ----------
#     datalist : TYPE
#         DESCRIPTION.
#     fichier : TYPE
#         DESCRIPTION.

#     Returns
#     -------
#     list of list 

#     """
    
#     with open(fichier,"w") as fich :
#         writer=csv.writer(fich,delimiter=";",lineterminator="\n")
#         writer.writerows(datalist)
#     return fichier

# def extraire_un_critere(datalist,variable, valeur):
#     """
#     Fonction pour extraire les lignes du datalist correspondant à un critère unique.
#     Args:
#         datalist (list of lists): Liste de données.
#         variable: nom de la variable.
#         valeur: Valeur du critère à correspondre.
#         fichier: fichier qui va contenir les resulats
#     Returns:
#        none
#     """
#     liste=[]
#     for ligne in datalist[1:]:
#         if ligne[Index_variable(datalist,variable)] == valeur:
#          liste.append(ligne)
#     return [datalist[0]]+liste

# def extraire_plus_critere(datalist):
#         data=datalist
#         variable=input("entrer la variable ou va s'appliquer le critére par exemple sexe ")
#         valeur=input("entrer le critére ")
#         data=extraire_un_critere(data,variable, valeur)
#         reponse=input("Voulez vous aplliqués un filtre O:N")
#         while reponse.upper()=="O" : 
#             variable=input("entrer la variable ou va s'appliquer le critére par exemple sexe(3) ")
#             valeur=input("entrer le critére ")
#             data=extraire_un_critere(data,variable, valeur)
#             reponse=input("Voulez vous aplliqués un filtre O:N")
#         return data  

# def les_valeurs(data,variable):
#     """
#     retourne une liste avec les toutes valeurs prises pour une variable 

#     Parameters
#     ----------
#     data : liste de liste 
       
#     variable : str
       

#     Returns
#     -------
#    liste 

#     """
#     liste=[]
#     for ligne in data[1:] :
#         liste.append(ligne[Index_variable(data, variable)])
#     return liste

# def les_modalites(data,var_quali):
#     """
#     retourne toutes les modalités d'une variables quantitative

#     Parameters
#     ----------
#     data : liste de liste 
       
#     variable : str
#         +

#     Returns
#     -------
#    liste

#     """
#     liste=[]
#     for i in range(len(data[0])):
#         if data[0][i]==var_quali :
#             for ligne in data[1:] :
#                 if ligne[i] not in liste:  
#                     liste.append(ligne[i])  #ici on aura ajout d'un element qui nexiste pas dans ma liste au préalabe
#     return liste
# def max_variable(data,variable_quanti):
#    """
#    Retourne la valeur maxiamle d'une variable quantitative.

#    Parameters
#    ----------
#    data : list of lists
#        Donnes sous forme de liste de listes.
#    variable_quanti : str
#        Nom de la colonne contenant la variable quantitative.

#    Returns
#    -------
#    float
#        Valeur minimale de la variable.
       
#    """
#    for i in range (len(data[0])):
#         if data[0][i]==variable_quanti :
#           maxval=0
#           for ligne in data[1:]:
#             if maxval<int(ligne[i]) :
#                 maxval=int(ligne[i])
#    return maxval

# def min_variable(data, variable_quanti):
#     """
#     Retourne la valeur minimale d'une variable quantitative.

#     Parameters
#     ----------
#     data : list of lists
#         Donnes sous forme de liste de listes.
#     variable_quanti : str
#         Nom de la colonne contenant la variable quantitative.

#     Returns
#     -------
#     float
#         Valeur minimale de la variable.
        
#     """
#     liste=[]
#     for i in range (len(data[0])):
#         if data[0][i]==variable_quanti :
#           for ligne in data[1:]:
#             liste.append(ligne[i])
#           minval=liste[0]
#           for element in liste :
#             if minval>int(element) :
#              minval=int(element)
#     return minval
   

# def moyenne_variable(data, variable_quanti):
#     """
#     Retourne la moyenne des valeurs d'une variable quantitative.

#     Parameters
#     ----------
#     data : list of lists
#         DonnÃ©es sous forme de liste de listes.
#     variable_quanti : str
#         Nom de la colonne contenant la variable quantitative.

#     Returns
#     -------
#     float
#         Moyenne de la variable.
#     """
#     liste=[]
#     somme=0
#     for i in range (len(data[0])):
#        if data[0][i]==variable_quanti :
#          for ligne in data[1:]:
#           liste.append(ligne[i])
#           somme=+int(ligne[i])
#     print(liste)
#     moyenne=somme/len(liste)
#     return round(moyenne,2)


# def total_variable(data, variable_quanti):
#     """
#     Retourne la somme des valeurs d'une variable quantitative.

#     Parameters
#     ----------
#     data : list of lists
#         DonnÃ©es sous forme de liste de listes.
#     variable_quanti : str
#         Nom de la colonne contenant la variable quantitative.

#     Returns
#     -------
#     float
#         Somme des valeurs de la variable.
#     """
   
#     somme=0
#     for i in range (len(data[0])):
#        if data[0][i]==variable_quanti :
#          for ligne in data[1:]:
#           somme=somme+int(ligne[i])
#     return somme 

# def effectifs_annee_metier_sexe(data,annee,metier,sexe) :
#     """
#     retourne l'effectif total par metier sexe et a une annee entrés par l'utilisateur 

#     Parameters
#     ----------
#     data : liste de liste 
        
#     annee : str
#       l'annee dont on veut les effectifs   
#     metier : str
#       le metier dont on veut l'effectif total'  
#     sexe : str
        
#       le sexe dont ont veut l'effectifs total'
#     Returns

#     -------
#     effectif_total:float

#     """
#     data_annee=extraire_un_critere(data,"annee",annee)
#     lignes_metier = extraire_un_critere(data_annee,"Métiers",metier)
#     lignes_sexe=extraire_un_critere(lignes_metier,"Sexe",sexe)
#     effectif_total =total_variable(lignes_sexe,"eff")
#     return effectif_total



# def repartition_eff_sexe_annee_metier(data,annee):
#     """
#     renvoie un tableau avec les effectifs total par sexe metier annee pour une annee 

#     Parameters
#     ----------
#     data : TYPE
#         DESCRIPTION.
#     annee : TYPE
#         DESCRIPTION.
#     fichier_sortie : TYPE
#         DESCRIPTION.

#     Returns
#     -------
#     tableau : liste 

#     """
    
#     entete= ["Métier", "Effectif total", "Effectif H", "Effectif F"]
#     tableau = [entete]   
#     metiers = les_modalites(data,"Métiers")
#     for metier in metiers:
#         effectif_h =effectifs_annee_metier_sexe(data, annee, metier,"Homme")
#         effectif_f =effectifs_annee_metier_sexe(data, annee, metier,"Femme")
#         tableau.append([metier, effectif_h+effectif_f, effectif_h, effectif_f])
#     return tableau 
# def effectifs_annee_metier(data,annee,metier) :
#     """
#      retourne l'effectif total d'un metier par sexe 

#     Parameters
#     ----------
#     data : liste de liste 
    
#     annee : str
        
#     metier : str
#         .
#     sexe : str 
       

#     Returns
#     -------
#     effectif_total:float

#     """
#     data_annee=extraire_un_critere(data,"annee",annee)
#     lignes_metier = extraire_un_critere(data_annee,"Métiers",metier)
#     effectif_total =total_variable(lignes_metier,"eff")
#     return effectif_total

# def Evolution_annee_metier(data):
#     """
#     Retourne un tableau avec les effectifs totaux par métier pour chaque année, ainsi que l'effectif moyen par métier.

#     Parameters
#     ----------
#     data : list
#         La liste de données à traiter. Chaque entrée de la liste contient des informations sur une année, un métier, un sexe, etc.

#     Returns
#     -------
#     tableau : list
#         Un tableau (liste de listes) où chaque ligne représente un métier et contient les effectifs par année, ainsi que l'effectif moyen pour ce métier.
#     """
#     annees = les_modalites(data, "annee")
#     entete = ["Métier"]
#     for annee in annees:
#         entete.append(annee)   
#     entete.append("Effectif_moyen") 
#     tableau = [entete]
#     metiers = les_modalites(data, "Métiers")
#     for metier in metiers:
#         ligne = [metier]
#         for annee in annees:
#             effectif_Total = effectifs_annee_metier(data, annee, metier)
#             ligne.append(effectif_Total)
#         somme = 0
#         for element in ligne[1:]:
#             somme += int(element)
#         effectif_moyen = round(somme / len(annees), 2)
#         ligne.append(effectif_moyen)
#         tableau.append(ligne)
#     fin = ["Effectif total"]
#     for annee in tableau[0][1:]:  # Je parcours la première ligne sans prendre l'en-tête métier
#         total = total_variable(tableau, annee)
#         fin.append(total)
#     tableau.append(fin)
#     return tableau


# def effectifs_annee_sexe(data, sexe, annee):
#     """
#     Calcule l'effectif total pour un sexe donné, une année et un ensemble de données.

#     Parameters
#     ----------
#     data : list
#         La liste de données à traiter.
#     sexe : str
#         Le sexe pour lequel on veut obtenir l'effectif total ("Homme" ou "Femme").
#     annee : str
#         L'année pour laquelle on veut obtenir l'effectif total.

#     Returns
#     -------
#     effectif_total : int
#         L'effectif total pour le sexe et l'année donnés.
#     """
#     data_annee = extraire_un_critere(data, "annee", annee)
#     lignes_sexe = extraire_un_critere(data_annee, "Sexe", sexe)
#     effectif_total = total_variable(lignes_sexe, "eff")
#     return effectif_total


# def Evolution_annee_sexe(data):
#     """
#     Retourne un tableau avec les effectifs totaux par sexe pour chaque année, ainsi que l'effectif moyen par sexe.

#     Parameters
#     ----------
#     data : list
#         La liste de données à traiter.

#     Returns
#     -------
#     tableau : list
#         Un tableau (liste de listes) où chaque ligne représente un sexe et contient les effectifs par année, ainsi que l'effectif moyen pour ce sexe.
#     """
#     annees = les_modalites(data, "annee")
#     entete = ["Sexe"]
#     for annee in annees:
#         entete.append(annee)   
#     entete.append("Effectif_moyen") 
#     tableau = [entete]
#     sexes = les_modalites(data, "Sexe")
#     for sexe in sexes:
#         ligne = [sexe]
#         for annee in annees:
#             effectif_Total = effectifs_annee_sexe(data, annee, sexe)
#             ligne.append(effectif_Total)
#         somme = 0
#         for element in ligne[1:]:
#             somme += int(element)
#         effectif_moyen = round(somme / len(annees), 2)
#         ligne.append(effectif_moyen)
#         tableau.append(ligne)
#     return tableau


# def effectifs_annee_contrat_sexe(data, annee, contrat, sexe):
#     """
#     Calcule l'effectif total pour un sexe donné, une année et un type de contrat.

#     Parameters
#     ----------
#     data : list
#         La liste de données à traiter.
#     annee : str
#         L'année pour laquelle on veut obtenir l'effectif total.
#     contrat : str
#         Le type de contrat 
#     sexe : str
#         Le sexe pour lequel on veut obtenir l'effectif total ("Homme" ou "Femme").

#     Returns
#     -------
#     effectif_total : int
#         L'effectif total pour le sexe, l'année et le type de contrat donnés.
#     """
#     data_annee = extraire_un_critere(data, "annee", annee)
#     lignes_contrat = extraire_un_critere(data_annee, "contrat", contrat)
#     lignes_sexe = extraire_un_critere(lignes_contrat, "Sexe", sexe)
#     effectif_total = total_variable(lignes_sexe, "eff")
#     return effectif_total


# def repartition_eff_contrat_sexe_annee(data, annee):
#     """
#     Calcule la répartition des effectifs par type de contrat et sexe pour une année donnée.

#     Parameters
#     ----------
#     data : list
#         La liste de données à traiter.
#     annee : str
#         L'année pour laquelle on veut obtenir la répartition des effectifs.

#     Returns
#     -------
#     tableau : list
#         Un tableau (liste de listes) avec les colonnes : Année, Contrat de travail, Nombres d'hommes, Nombres de femmes.
#     """
#     entete = ["Annee", "Contrat de travail", "Nombres d'hommes", "Nombres de femmes"]
#     tableau = [entete]   
#     contrats = les_modalites(data, "contrat")

#     for contrat in contrats:
#         effectif_h = effectifs_annee_contrat_sexe(data, annee, contrat, "Homme")
#         effectif_f = effectifs_annee_contrat_sexe(data, annee, contrat, "Femme")
#         tableau.append([annee, contrat, effectif_h, effectif_f])
#     return tableau


# def max_effectif_par_sexe(data, annee):
#     """
#     Fonction qui domme  le plus grand nombre d'effectifs par sexe (homme et femme)
#     pour une année donnée de chaque metier

#     Parameters
#     ----------
#     data : list of lists
#         Données sous forme de liste de listes.
#     annee : str
#         L'année pour laquelle les effectifs doivent être extraits.

#     Returns
#     -------
#     tableau : list of lists
#         Tableau contenant les métiers et les effectifs par sexe pour l'année spécifiée.
#     """
#     tableau = [["Métier", "Effectif Homme", "Effectif Femme"]]  
#     data_annee = extraire_un_critere(data,"annee", annee) 
#     metiers = les_modalites(data, "Métiers")
#     for metier in metiers:
#         lignes_metier = extraire_un_critere(data_annee,"Métiers", metier)
#         lignes_metier_f=extraire_un_critere(lignes_metier,"Sexe","Femme")
#         lignes_metier_h=extraire_un_critere(lignes_metier,"Sexe","Homme")
#         effectif_homme = max_variable(lignes_metier_h, "eff")
#         effectif_femme = max_variable(lignes_metier_f, "eff")
#         tableau.append([metier, effectif_homme, effectif_femme])
#     return tableau

# def min_effectif_par_sexe(data, annee):
#     """
#     Fonction qui donne le plus petit nombre d'effectifs par sexe (homme et femme)
#     pour une année donnéepar metier

#     Parameters
#     ----------
#     data : list of lists
#         Données sous forme de liste de listes.
#     annee : str
#         L'année pour laquelle les effectifs doivent être extraits.

#     Returns
#     -------
#     tableau : list of lists
#         Tableau contenant les métiers et les effectifs par sexe pour l'année spécifiée.
#     """
#     tableau = [["Métier", "Effectif Homme", "Effectif Femme"]]  
#     data_annee = extraire_un_critere(data,"annee", annee) 
#     metiers = les_modalites(data, "Métiers")
#     for metier in metiers:
#         lignes_metier = extraire_un_critere(data_annee,"Métier", metier)
#         lignes_metier_f=extraire_un_critere(lignes_metier,"Sexe","Femme")
#         lignes_metier_h=extraire_un_critere(lignes_metier,"Sexe","Homme")
#         effectif_homme = min_variable(lignes_metier_h,"eff")
#         effectif_femme = min_variable(lignes_metier_f,"eff")
#         tableau.append([metier, effectif_homme, effectif_femme])
#     return tableau
# def moyenne_recrutement_sexe_metier(data,annee_debut,annee_fin):
    
#     #A refaire entre deux année 
#     """
#      la moyenne des recrutements par métier et sexe
#      entre deux année

#     Parameters
#     ----------
#     data : list of lists
#         Données sous forme de liste de listes.
    
#     """
#     colonnes = ["Métier", "Moyenne Totale", "Moyenne Homme", "Moyenne Femme"]
#     tableau = [colonnes]
#     metiers = les_modalites(data, "Métiers")
#     data_annee= [data[0]]
#     for ligne in data[1:] :
#         if int(ligne[0]) >= annee_debut and int(ligne[0]) <= annee_fin :
#            data_annee.append(ligne) 
#     for metier in metiers:
#         lignes_metier = extraire_un_critere(data_annee,1, metier)
#         print(lignes_metier)
#         moyenne_totale = moyenne_variable(lignes_metier, "recru")
#         lignes_metier_h = extraire_un_critere(lignes_metier,"Sexe", "Homme")
#         print(lignes_metier_h)
#         moyenne_homme = moyenne_variable(lignes_metier_h, "recru")
#         lignes_metier_f = extraire_un_critere(lignes_metier,"Sexe", "Femme")
#         print(lignes_metier_f)
#         moyenne_femme = moyenne_variable(lignes_metier_f, "recru")
#         tableau.append([metier, moyenne_totale, moyenne_homme, moyenne_femme])
#     return tableau
    
# def annee_max_effectifs_par_metier_et_sexe(data):
#     """
#     Retourne les années avec le plus grand nombre de recrutements par métier et par sexe.

#     Parameters
#     ----------
#     data : list of lists
#         Données sous forme de liste de listes (incluant années, métiers, sexe et effectifs).
#     fichier_sortie : str
#     le fichier CSV de sortie.

#     Returns
#     -------
#     None
#     """
#     colonnes = ["Métier", "Sexe", "Année", "Effectif maximal"]
#     tableau = [colonnes]
#     metiers = les_modalites(data, "Métiers")
#     sexes = les_modalites(data, "Sexe")
#     for metier in metiers:
#         for sexe in sexes:
            
#             lignes_metier= extraire_un_critere(data,"Métiers", metier)
#             lignes_metier_sexe = extraire_un_critere(lignes_metier,"Sexe", sexe)
#             print(lignes_metier_sexe)
#             max_eff = max_variable(lignes_metier_sexe,"eff")
#             for ligne in lignes_metier_sexe[1:]:
#                 if int(ligne[4]) == max_eff:
#                   annee = ligne[0]
#                   tableau.append([metier, sexe, annee, max_eff])
#                   break

    
#     return tableau




# def annee_min_recrutements_par_metier_et_sexe(data):
#     """
#     Retourne les années avec le plus grand nombre de recrutements par métier et par sexe.

#     Parameters
#     ----------
#     data : list of lists
#         Données sous forme de liste de listes (incluant années, métiers, sexe et effectifs).
  
#     Returns
#     -------
#     list of list
#     """
#     colonnes = ["Métier", "Sexe", "Année", "Recrutement maximal"]
#     tableau = [colonnes]
#     metiers = les_modalites(data, "Métiers")
#     sexes = les_modalites(data, "Sexe")
#     for metier in metiers:
#         for sexe in sexes:
            
#             lignes_metier= extraire_un_critere(data,"Métiers", metier)
#             lignes_metier_sexe = extraire_un_critere(lignes_metier,"Sexe", sexe)
#             print(lignes_metier_sexe)
#             max_recru = min_variable(lignes_metier_sexe,"recru")
#             for ligne in lignes_metier_sexe[1:]:
#                 if int(ligne[4]) == max_recru:
#                   annee = ligne[0]
#                   tableau.append([metier, sexe, annee, max_recru])
#                   break

    
#     return tableau

# def evolution_recrutements_entre_deux_année(data, annee_debut, annee_fin):
#     """
#     Calcule l'évolution des recrutements par métier et par sexe en pourcentage.

#     Parameters
#     ----------
#     data : list of lists
#         Données sous forme de liste de listes.
#     annee_debut : str
#         Année de début 
#     annee_fin : str
#         Année de fin 

#     Returns
#     -------
#     list of lists
#         Tableau contenant l'évolution des recrutements par métier et par sexe.
#     """
#     colonnes = ["Métier", "Sexe","Recrutements debut ","Recrutements fin", "Évolution (%)"]
#     tableau = [colonnes]
#     metiers = les_modalites(data, "Métiers")
#     sexes = les_modalites(data, "Sexe")
#     for metier in metiers:
#         for sexe in sexes:
#             data_debut_annee = extraire_un_critere(data,"annee", annee_debut)
#             data_debut_annee_metier=extraire_un_critere(data_debut_annee,"Métiers",metier)
#             data_debut= extraire_un_critere(data_debut_annee_metier,"Sexe", sexe)
#             print(data_debut)
#             data_fin_annee = extraire_un_critere(data,"annee", annee_fin)
#             data_fin_annee_metier=extraire_un_critere(data_fin_annee,"Métiers",metier)
#             data_fin= extraire_un_critere(data_fin_annee_metier,"Sexe", sexe)
#             print(data_fin)
#             recrutements_debut = total_variable(data_debut, "recru")
#             recrutements_fin = total_variable(data_fin, "recru")
#             if not recrutements_debut==0 :
#              evolution = ((recrutements_fin - recrutements_debut) / recrutements_debut) * 100
#              tableau.append([metier,sexe,recrutements_debut,recrutements_fin,round(evolution, 2)])
    
#     return tableau

# def evolution_effectifs_entre_deux_année(data, annee_debut, annee_fin):
#     """
#     Calcule l'évolution des recrutements par métier et par sexe en pourcentage.

#     Parameters
#     ----------
#     data : list of lists
#         Données sous forme de liste de listes.
#     annee_debut : str
#         Année de début 
#     annee_fin : str
#         Année de fin 

#     Returns
#     -------
#     list of lists
#         Tableau contenant l'évolution des recrutements par métier et par sexe.
#     """
#     entete = ["Métier", "Sexe","effectifs debut ","effectifs fin", "Évolution (%)"]
#     tableau = [entete]
#     metiers = les_modalites(data, "Métiers")
#     sexes = les_modalites(data, "Sexe")
#     for metier in metiers:
#         for sexe in sexes:
#             data_debut_annee = extraire_un_critere(data,"annee", annee_debut)
#             data_debut_annee_metier=extraire_un_critere(data_debut_annee,"Métiers",metier)
#             data_debut= extraire_un_critere(data_debut_annee_metier,"Sexe", sexe)
#             print(data_debut)
#             data_fin_annee = extraire_un_critere(data,"annee", annee_fin)
#             data_fin_annee_metier=extraire_un_critere(data_fin_annee,"Métiers",metier)
#             data_fin= extraire_un_critere(data_fin_annee_metier,"Sexe", sexe)
#             print(data_fin)
#             effectifs_debut = total_variable(data_debut, "eff")
#             effectifs_fin = total_variable(data_fin, "eff")
#             if effectifs_debut!=0 :
#              evolution = ((effectifs_fin - effectifs_debut) / effectifs_debut) * 100
#              tableau.append([ metier, sexe,effectifs_debut,effectifs_fin,round(evolution, 2)])
    
#     return tableau

# def creer_fichiers_evolution_effectif(data):
#     """
#     Crée les fichiers CSV pour l'évolution des effectifs :
#     - Par métier
#     - Par métier pour les femmes
#     - Par type de contrat
#     Enregistre les résultats dans le dossier EXPORT/STATISTIQUES/Evolution_effectif.
    
#     Parameters
#     ----------
#     data : list of lists
#         Données des effectifs sous forme de liste de listes.
    
#     Returns
#     -------
#     None
#     """
#     # Evolution des effectifs par métier
#     evolution_par_metier = evolution_effectifs_entre_deux_année(data, "2012", "2023")
#     exporter(evolution_par_metier, "EXPORT/STATISTIQUES/Evolution_effectif/Evolution_effectif_par_metier.csv")

#     # Evolution des effectifs par métier pour les femmes
#     evolution_femmes = extraire_un_critere(data, "Sexe", "Femme")
#     evolution_femmes_par_metier = evolution_effectifs_entre_deux_année(evolution_femmes, "2012", "2023")
#     exporter(evolution_femmes_par_metier, "EXPORT/STATISTIQUES/Evolution_effectif/Evolution_effectif_femme_par_metier.csv")
    
#     print("Fichiers d'évolution des effectifs créés dans EXPORT/STATISTIQUES/Evolution_effectif")


# def top_metiers_recrutements(data, annee, type_contrat,n):
#     """
#     Fonction qui récupère les n métiers ayant le plus grand nombre de recrutements
#     pour une année, un type de contrat et un sexe donnés.

#     Parameters
#     ----------
#     data : list of lists
#         Données sous forme de liste de listes.
#     annee : str
        
#     type_contrat : str
#         Le type de contrat 
#     sexe : str
#         Le sexe 
#     n : int
#         Nombre de métiers 

#     Returns
#     -------
#     tableau : list of lists
#         Tableau contenant les métiers et leurs recrutements pour les critères spécifiés.
#     """
#     entete = [["Métier", "Total Recrutements"]]
#     tableau = []
#     data_annee = extraire_un_critere(data,"annee", annee)
#     print(data_annee)
#     data_contrat = extraire_un_critere(data_annee,"contrat", type_contrat)
#     print(data_contrat)
#     data_sexe = extraire_un_critere(data_contrat,"Sexe","Homme")
#     print(data_sexe)
#     metiers = les_modalites(data_sexe, "Métiers")
#     print(metiers)
#     for metier in metiers:
#         lignes_metier = extraire_un_critere(data_sexe,"Métiers", metier)
#         print(lignes_metier)
#         total_recrutements = total_variable(lignes_metier, "recru")
#         tableau.append([metier, total_recrutements])
#     tableau.sort()
#     tableau_final = entete + tableau
#     return tableau_final[:n+1]# Retourner les n premiers resultats avec l'entête



# def menu():
#     """
#     Affiche un menu général pour l'exploitation des données SNCF et retourne le choix de l'utilisateur.
#     """
#     print("=" * 70)
#     print("Exploitation des données effectifs et recrutement SNCF")
#     print("------------------------- MENU GENERAL -------------------------")
#     print("2. Données : Description globale (qualité & quantité)")
#     print("3. Visualisation : Affichage des données")
#     print("4. Extraire un critère")
#     print("5. Extraire plusieurs critères")
#     print("6. Effectif total par année, métier et sexe")
#     print("7. Répartition des effectifs par sexe, année et métier")
#     print("8. Effectifs total par année et métier")
#     print("9. Évolution des effectifs par année et métier")
#     print("10. Effectifs total par année et sexe")
#     print("11. Évolution des effectifs par année et sexe")
#     print("12. Effectifs total par contrat, sexe et année")
#     print("13. Maximum des effectifs par sexe pour une année donnée")
#     print("14. Minimum des effectifs par sexe pour une année donnée")
#     print("15. Moyenne des recrutements par sexe et métier")
#     print("16. Année avec effectifs maximaux par métier et sexe")
#     print("17. Année avec recrutements minimaux par métier et sexe")
#     print("18. Évolution des recrutements entre deux années")
#     print("19. Évolution des effectifs entre deux années")
#     print("20. Top métiers par recrutements pour un type de contrat")
#     print("21.Vérification Résultat Répartition sexe ")
#     print("0. Quitter")
#     print("=" * 70)
#     choix = int(input("Entrez le numéro de votre choix : "))
#     return choix


# def gestion():
#     """
#     Effectue le choix d'un utilisateur 
#     """

#     choix = menu()  
    
#     if choix == 2:
#         print("Il s'agit d'une application qui permet l'analyse des fichiers csv des recrutements et des effectifs de la SNCF de 2012 à 2023 suivant une répartition par sexe, contrat, métiers et années.")
    
#     elif choix == 3:
#         afficher(effectifs)
#         afficher(recrutements)
    
#     elif choix == 4:
#         reponse = input("Voulez-vous extraire un critère sur les effectifs ou les recrutements ? ")
#         if reponse == "effectifs":
#             variable = input("Entrez le nom de la variable : ")
#             valeur = input("Entrez la valeur : ")
#             print(extraire_un_critere(effectifs, variable, valeur)) 
#         elif reponse == "recrutements":
#             variable = input("Entrez le nom de la variable : ")
#             valeur = input("Entrez la valeur : ")
#             print(extraire_un_critere(recrutements, variable, valeur)) 
    
#     elif choix == 5:
#         reponse = input("Voulez-vous extraire plusieurs critères sur les effectifs ou les recrutements ? ")
#         if reponse == "effectifs":
#             print(extraire_plus_critere(effectifs))
#         elif reponse == "recrutements":
#             print(extraire_plus_critere(recrutements))
    
#     elif choix == 6:
#         metier = input("Entrez le métier : ")
#         sexe = input("Entrez le sexe : ")
#         annee = int(input("Entrez l'année : "))
#         tableau = effectifs_annee_metier_sexe(effectifs, annee, metier, sexe)
#         afficher(tableau)
#         exporter(tableau, f"EXPORT/STATISTIQUES/effectifs_{metier}_{sexe}_{annee}.csv")
    
#     elif choix == 7:
#         annee = input("Entrez l'année : ")
#         tableau = repartition_eff_sexe_annee_metier(effectifs, annee)
#         afficher(tableau)
#         exporter(tableau, f"EXPORT/STATISTIQUES/repartition_eff_sexe_{annee}_metier_{annee}.csv")
    
#     elif choix == 8:
#         annee = input("Entrez l'année : ")
#         tableau = effectifs_annee_metier(effectifs, annee)
#         afficher(tableau)
#         exporter(tableau, f"EXPORT/STATISTIQUES/effectifs_annee_metier_{annee}.csv")
    
#     elif choix == 9:
#         tableau = Evolution_annee_metier(effectifs)
#         afficher(tableau)
#         exporter(tableau, "EXPORT/STATISTIQUES/evolution_annee_metier.csv")
    
#     elif choix == 10:
#         annee = input("Entrez l'année : ")
#         sexe = input("Entrez le sexe (Homme/Femme) : ")
#         tableau = effectifs_annee_sexe(effectifs, annee, sexe)
#         afficher(tableau)
#         exporter(tableau, f"EXPORT/STATISTIQUES/effectifs_{sexe}_{annee}.csv")
    
#     elif choix == 11:
#         tableau = Evolution_annee_sexe(effectifs)
#         afficher(tableau)
#         exporter(tableau, f"EXPORT/STATISTIQUES/evolution_{annee}_sexe.csv")
    
#     elif choix == 12:
#         annee = input("Entrez l'année : ")
#         sexe = input("Entrez le sexe (Homme/Femme) : ")
#         contrat = input("Entrez le type de contrat de travail : ")
#         tableau = effectifs_annee_contrat_sexe(effectifs, annee, contrat, sexe)
#         afficher(tableau)
#         exporter(tableau, f"EXPORT/STATISTIQUES/effectifs_{sexe}_{contrat}_{annee}.csv")
    
#     elif choix == 13:
#         annee = input("Entrez l'année : ")
#         tableau = max_effectif_par_sexe(effectifs, annee)
#         afficher(tableau)
#         exporter(tableau, f"EXPORT/STATISTIQUES/max_effectif_par_sexe_{annee}.csv")
    
#     elif choix == 14:
#         annee = input("Entrez l'année : ")
#         tableau = min_effectif_par_sexe(effectifs, annee)
#         afficher(tableau)
#         exporter(tableau, f"EXPORT/STATISTIQUES/min_effectif_par_sexe_{annee}.csv")
    
#     elif choix == 15:
#         annee_debut = input("Entrez l'année de début : ")
#         annee_fin = input("Entrez l'année de fin : ")
#         tableau = moyenne_recrutement_sexe_metier(recrutements, annee_debut, annee_fin)
#         afficher(tableau)
#         exporter(tableau,f"EXPORT/STATISTIQUES/moyenne_recrutement_{annee_debut}_{annee_fin}_sexe_metier.csv")
    
#     elif choix == 16:
#         tableau = annee_max_effectifs_par_metier_et_sexe(effectifs)
#         afficher(tableau)
#         exporter(tableau, "EXPORT/STATISTIQUES/annee_max_effectifs_par_metier_et_sexe.csv")
    
#     elif choix == 17:
#         tableau = annee_min_recrutements_par_metier_et_sexe(recrutements)
#         afficher(tableau)
#         exporter(tableau, "EXPORT/STATISTIQUES/annee_min_recrutements_par_metier_et_sexe.csv")
    
#     elif choix == 18:
#         annee_debut = input("Entrez l'année de début : ")
#         annee_fin = input("Entrez l'année de fin : ")
#         tableau = evolution_recrutements_entre_deux_année(recrutements, annee_debut, annee_fin)
#         afficher(tableau)
#         exporter(tableau, f"EXPORT/STATISTIQUES/evolution_recrutements_{annee_debut}_{annee_fin}.csv")
    
#     elif choix == 19:
#         annee_debut = input("Entrez l'année de début : ")
#         annee_fin = input("Entrez l'année de fin : ")
#         tableau = evolution_effectifs_entre_deux_année(effectifs, annee_debut, annee_fin)
#         afficher(tableau)
#         exporter(tableau, f"EXPORT/STATISTIQUES/evolution_effectifs_{annee_debut}_{annee_fin}.csv")
    
#     elif choix == 20:
#         n = input("Vous voulez le top n ? ")
#         annee = input("Entrez l'année de votre tri : ")
#         contrat = input("Vous voulez le top n de quel type de contrat ? ")
#         tableau = top_metiers_recrutements(recrutements, annee, contrat, n)
#         afficher(tableau)
#         exporter(tableau, f"EXPORT/STATISTIQUES/top_{n}_metiers_recrutements_{annee}_{contrat}.csv")
    
#     elif choix==21:
#       annee=input("Entrer l'année du fichier effectifs avec lequel vous voulez comparé avec le fichier répartition par genre ")
#       tableau=repartition_eff_contrat_sexe_annee(effectifs,annee)
#       print(tableau)
#       exporter(tableau,f"EXPORT/STATISTIQUES/repartition_genre_effectifs_{annee}.csv")

     

# """APLLICATION """
# effectifs = importer("DATA/effectifs.csv")
# recrutements = importer("DATA/recrutements.csv")
# print("Bienvenu dans notre application d'analyse de fichier csv issus de la SNCF ")
# menu()
# gestion()

 
# "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"


   
# """Programme"""

# # effectifs=importer("DATA/effectif-metiers-sncf.csv")
# # afficher(effectifs)
# # renommer_variables(effectifs)
# # exporter(effectifs,"DATA/effectifs.csv")
# # recrutements=importer("DATA/recrutement-metiers-sncf.csv")
# # afficher(recrutements)
# # renommer_variables(recrutements)
# # exporter(recrutements,"DATA/recrutements.csv")
# # effectifs=importer("DATA/effectifs.csv")
# # recrutements=importer("DATA/recrutements.csv")
# # repartitions=importer("DATA/repartition-genre-effectif.csv")
# """test des 6 fonctions"""
# # minval=min_variable(effectifs, "eff")
# # print(minval)
# # maxval=max_variable(effectifs, "eff")
# # print(maxval)
# # moyenne=moyenne_variable(effectifs,"eff")
# # print(moyenne)
# # total=total_variable(effectifs, "eff")
# # print(total)
# # valeurs=les_valeurs(effectifs, 0)
# # print(valeurs)
# # modalites=les_modalites(effectifs,"Sexe")
# # print(modalites)
# """test de fonction d'analyse"""
# # repartition_2012=repartition_eff_sexe_annee_metier(effectifs,"2012")
# # print(repartition_2012)
# # exporter(repartition_2012,"EXPORT/STATISTIQUES/repartition_2012.csv")
# # tableau=Evolution_annee_metier(effectifs)
# # print(tableau)
# # exporter(tableau,"EXPORT/STATISTIQUES/Evolution_effectif_metier.csv")
# # Evolution_par_sexe=Evolution_annee_sexe(effectifs)
# # print(Evolution_par_sexe)
# # exporter(Evolution_par_sexe,"EXPORT/STATISTIQUES/Evolution_effectif_sexe.csv")
# # max_eff_sexe_2023=max_effectif_par_sexe(effectifs,"2023")
# # exporter(max_eff_sexe_2023,"EXPORT/STATISTIQUES/max_eff_metier_2023.csv")
# # max_eff_sexe_2012=max_effectif_par_sexe(effectifs,"2012")
# # exporter(max_eff_sexe_2012,"EXPORT/STATISTIQUES/max_eff_metier_2012.csv")
# # min_eff_sexe_2012=min_effectif_par_sexe(effectifs,"2012")
# # exporter(min_eff_sexe_2012,"EXPORT/STATISTIQUES/min_eff_metier_2012.csv")
# #moyenne_recrutement_sexe_metier(recrutements,"EXPORT/STATISTIQUES/moyenne_recru_2012_2023.csv")
# # annee_max_recrutements_par_metier_et_sexe(recrutements,"EXPORT/STATISTIQUES/max_recru_2012_2023.csv")
# # annee_max_effectifs_par_metier_et_sexe(effectifs,"EXPORT/STATISTIQUES/max_eff_2012_2023.csv")
# # annee_min_recrutements_par_metier_et_sexe(recrutements,"EXPORT/STATISTIQUES/min_recru_2012_2023.csv")
# # annee_min_effectifs_par_metier_et_sexe(effectifs,"EXPORT/STATISTIQUES/min_eff_2012_2023.csv")
# # evolution_effectifs=evolution_effectifs_entre_deux_année(effectifs,"2012","2023")
# # exporter(evolution_effectifs,"EXPORT/STATISTIQUES/Evolution_eff_2012_2023.csv")
# # evolution_recrutements=evolution_recrutements_entre_deux_année(recrutements,"2022","2023")
# # exporter(evolution_recrutements,"EXPORT/STATISTIQUES/Evolution_recru_2012_2023.csv")
# #nombre_recru_par_contrat_metier(recrutements,"2023","EXPORT/STATISTIQUES/nombre_recru_de_contrat_2023.csv")
# #ne marche pas également
# # top3_metier_HommeCP2023_recrutements=top_metiers_recrutements(recrutements,"2023","Cadre permanent",3)
# # exporter(top3_metier_HommeCP2023_recrutements,"EXPORT/STATISTIQUES/top3_metier_HommeCP2023_recrutements.csv")
# # repartition_contrat=repartition_eff_contrat_sexe_annee(effectifs)
# # print(repartition_contrat)
# #exporter(repartition_contrat,"EXPORT/STATISTIQUES/repartition_genre_effectifs_SNCF_analyse.csv")
# # Evolution_effectif=Evolution_annee_metier(effectifs)
# # print(Evolution_effectif)

# """implémentation des indicateurs comparatifs  obtenus avec les indicateurs fournis par la snfc repartition"""

# # tableau=repartition_eff_contrat_sexe_annee(effectifs,"2015")
# # print(tableau)
# # exporter(tableau,"EXPORT/STATISTIQUES/repartition_genre_effectifs_2015.csv")


# # tableau=repartition_eff_contrat_sexe_annee(effectifs,"2013")
# # print(tableau)
# # exporter(tableau,"EXPORT/STATISTIQUES/repartition_genre_effectifs_2013.csv")

# # tableau=repartition_eff_contrat_sexe_annee(effectifs,"2016")
# # print(tableau)
# # exporter(tableau,"EXPORT/STATISTIQUES/repartition_genre_effectifs_2017.csv")

# # tableau=repartition_eff_contrat_sexe_annee(effectifs,"2022")
# # print(tableau)
# # exporter(tableau,"EXPORT/STATISTIQUES/repartition_genre_effectifs_2022.csv")

# # tableau=repartition_eff_contrat_sexe_annee(effectifs,"2019")
# # print(tableau)
# # exporter(tableau,"EXPORT/STATISTIQUES/repartition_genre_effectifs_2019.csv")


# """extraction"""
# # femme_2012=extraire_plus_critere(effectifs)
# # print(femme_2012)
# # exporter(femme_2012,"EXPORT/EXTRACTIONS/Femme_2012.csv")
# # homme_2023_Cadre_permanent=extraire_plus_critere(effectifs)
# # print(homme_2023_Cadre_permanent)
# # exporter(homme_2023_Cadre_permanent,"EXPORT/EXTRACTIONS/homme_2023_Cadre_permanent.csv")
# # homme=extraire_un_critere(effectifs,3,"Homme")
# # print(homme)
# # exporter(homme,"EXPORT/EXTRACTIONS/homme.csv")

import pandas as pd
import matplotlib.pyplot as plt

chemin_fichier = "C:/Users/Nya Devas/Desktop/SAE_Cinema/APPLICATION/EXPORT/STATISTIQUES/tout_materiel_par_region.csv"

# ✅ Utilisez le bon séparateur
df = pd.read_csv(chemin_fichier, sep=';')

# ✅ Nettoyez les noms de colonnes
df.columns = df.columns.str.strip()

# ✅ Affichez les noms pour vérifier
print(df.columns)

plt.figure(figsize=(10, 10))
regions = df["Région"].unique()
for region in regions:
    sous_df = df[df["Région"] == region]
    plt.plot(sous_df["Année"], sous_df["Nombre de cinémas"], marker='o', label=region)
plt.title("🎬 Évolution du nombre de cinémas par région")
plt.xlabel("Année")
plt.ylabel("Nombre de cinémas")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 📊 2. Nombre d’écrans par année
plt.figure(figsize=(10, 10))
regions = df["Région"].unique()
for region in regions:
    sous_df = df[df["Région"] == region]
    plt.plot(sous_df["Année"], sous_df["Nombre d'écrans"], marker='o', label=region)
plt.title("🎬 Évolution du nombre d'écrans par région")
plt.xlabel("Année")
plt.ylabel("Nombre d'écrans")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 📊 2. Nombre de fauteuils par année
plt.figure(figsize=(10, 10))
regions = df["Région"].unique()
for region in regions:
    sous_df = df[df["Région"] == region]
    plt.plot(sous_df["Année"], sous_df["Nombre de fauteuils"], marker='o', label=region)
plt.title("🎬 Évolution du nombre de fauteuils par région")
plt.xlabel("Année")
plt.ylabel("Nombre de fauteuils")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 📊 2. Nombre de séances par année
plt.figure(figsize=(10, 10))
regions = df["Région"].unique()
for region in regions:
    sous_df = df[df["Région"] == region]
    plt.plot(sous_df["Année"], sous_df["Nombre de séances"], marker='o', label=region)
plt.title("🎬 Évolution du nombre de séances par région")
plt.xlabel("Année")
plt.ylabel("Nombre de seance")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 📊 2. Nombre d'entrées par année
plt.figure(figsize=(10, 10))
regions = df["Région"].unique()
for region in regions:
    sous_df = df[df["Région"] == region]
    plt.plot(sous_df["Année"], sous_df["Nombre d'entrées"], marker='o', label=region)
plt.title("🎬 Évolution du nombre d'entrées par région")
plt.xlabel("Année")
plt.ylabel("Nombre de seance")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()