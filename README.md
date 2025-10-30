# Analyse-des-donn-es-RH-de-la-SNCF-Open-data-
Concevoir et développer une application capable de lire, transformer et enregistrer des flux de données, en suivant des consignes précises, afin de produire des informations exploitables pour la prise de décision.
Activités réalisées
Sujet : Traitement des données ouvertes de la SNCF : Les métiers, les effectifs et les recrutements depuis 2012. « Focus sur la répartition par genre » 

Compréhension des besoins de la SAE et découverte des données issus des open data de la SNCF
- Lecture , compréhension du sujet et des besoins du commanditaire
-Téléchargement et familiarisation aux deux jeux de données mis à notre disposition sur le site (recrutement-metiers-sncf.csv, effectif-metiers-sncf.csv)
- Compréhension des méta données (variables) et analyse des anomalies
- Création d’une arborescence pour structurer notre travail (dossier et sous dossiers)

Réflexion sur les différentes extractions de données par un ou par plusieurs critères pour évaluer certaines tendances des recrutements et des effectifs au sein de la SNCF
-Création d'une fonction pour importer les fichiers CSV contenant les données.
-Création d'une fonction pour afficher les données importées sous forme de liste dans l'interface.
-Rédaction de petits programmes utiles pour le reste du projet, par exemple :
o	index_variable(nom_variable) : donne la position (l'index) d'un nom de variable choisi par l'utilisateur.
o	les_valeurs(data, variable) : donne toutes les valeurs prises par une variable.
o	les_modalites(data, var_quali) : donne toutes les réponses possibles d'une variable qualitative.
o	total_variable(data, variable_quanti) : fait la somme des valeurs d'une variable numérique.
-Création de fonctions pour extraire des informations précises, selon un ou plusieurs critères :
•	effectifs_annee_metier_sexe(data, annee, metier, sexe) : donne le nombre total de personnes selon une année, un métier      et un sexe.
•	effectifs_annee_metier(data, annee, metier) : donne le nombre total de personnes pour un métier et une année donnés.
•	effectifs_annee_contrat_sexe(data, annee, contrat, sexe) : donne le nombre total de personnes selon une année, un contrat et un sexe.
-Exportation des résultats via une fonction préalablement écrite

Calculer les indicateurs et exporter des statistiques répondant aux besoins
-Développement de fonctions pour calculer des indicateurs simples :
o	max_variable(data, variable_quanti) : valeur maximale d’une variable quantitative.
o	min_variable(data, variable_quanti) : valeur minimale.
o	moyenne_variable(data, variable_quanti) : moyenne.
-Création de fonctions pour des analyses plus spécifiques :
o	max_effectif_par_sexe(data, annee) : plus grand nombre d’effectifs par sexe pour chaque métier, une année donnée.
o	min_effectif_par_sexe(data, annee) : plus petit nombre d’effectifs par sexe pour une année et un métier.
o	moyenne_recrutement_sexe_metier(data, annee_debut, annee_fin) : moyenne des recrutements par sexe et métier sur une période.
o	annee_max_effectifs_par_metier_et_sexe(data) : année avec le plus grand effectif pour chaque métier et sexe.
o	evolution_recrutements_entre_deux_annees(data, annee_debut, annee_fin) : évolution en pourcentage des recrutements par sexe et métier entre deux années.
-Exportation des résultats finaux dans des fichiers Excel pour une meilleure lisibilité et exploitation.

Comparaison des résultats obtenues avec le fichier répartitions de la SNCF
Visualisation des résultats à l’aide de module d’analyse sur Python
-Utilisation de pandas , seaborn et mathplotlib pour faire des graphiques permettant la compréhension plus simples des indicateurs calculés
Présentation orale écrite :
- réalisation d’un cahier de charge
- soutenance orale
