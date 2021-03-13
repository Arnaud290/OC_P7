++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# PROJET 7 : Résolvez des problèmes en utilisant des algorithmes en Python

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## Contexte

Création de deux algorithmes en language Python ("bruteforce.py" et "optimized.py")
permettant le test des possibilités d'achats d'actions. 

## Installation


### 1 - Installation de Python3, l'outil d'environnement virtuel et le gestionnaire de paquets (sur Linux UBUNTU)
    

    $ sudo apt-get install python3 python3-venv python3-pip


### 2 - Mise en place de l'environnement virtuel "env"


    1 - Accès au répertoire du projet :
            
            exemple cd /Actions_Tests

    2 - Création de l'environnement virtuel :
            
            $ python3 -m venv env


### 3 - Ouverture de l'environnement virtuel et ajout des modules


            $ source env/bin/activate
            
            (env) $ pip install -r requirements.txt
            

## Utilisation du programme


### 1 - Lancement


            $ python3 main.py


### 2 - Utilisation


    1 - Méthode en brute force pour 20 actions

            Lancement de l'alogrithme brutforce.py pour la liste de 20 actions "20_actions.csv"

    2 - Méthode optimisé pour 20 actions

            Lancement de l'alogrithme optimized.py pour la liste de 20 actions "20_actions.csv"

    3 - Méthode optimisé pour la liste compléte d'action

            Lancement de l'alogrithme optimized.py pour la liste de 20 actions "dataset2.csv"

    4 - Edition fichier csv temps d'exectution en fonction du nombre d'actions sur 40 actions en brut force

            test de l'alogrithme brutforce.py pour une liste de 40 actions "test_40_actions.csv" et retour des resultats 
            (nombre d'iterations, nombre d'actions traités et temps) dans un fichier csv "bruteforce_buy_actions.csv" 

    5 - Edition fichier csv temps d'exectution en fonctiondu nombre d'actions sur 40 actions en optimisé

            test de l'alogrithme optimized.py pour une liste de 40 actions "test_40_actions.csv" et retour des resultats 
            (nombre d'iterations, nombre d'actions traités et temps) dans un fichier csv "optimized_buy_actions.csv" 

    6 - Quitter
