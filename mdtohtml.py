# !/usr/bin/python3
import markdown
import os
import sys
import subprocess

# Création du Menu principal
def menu():
	print("Bienvenue dans le programme de conversion Markdown en HTML, /n 1 - Utiliser l'outil de conversion (!! Vous devez installer la bibliothèque Markdown et/ou Markdown2 dans Python !! /n 2 - Aide pour utiliser l'outil")
	print("Sélectionnez le choix 1 pour utiliser l'outil de conversion")
	print("Sélectionnez le choix 2 si vous avez besoin d'aide")
	choice = int(input())

# Création du choix 1
if choice == "1":
	fichier = input("Merci de sélectionner le fichier Markdown à convertir (markdown.md) : ")
	os.system("python -m markdown " + fichier + " > index.html")

# Création du choix 2
elif choice == "2":
	print("HELP - L'outil de conversion est simple à utiliser, /n Il vous suffit dans un premier temps de sélectionner le choix 1 pour acceder au convertisseur /n Ensuite tapez le nom de votre fichier (exemple: Markdown.md) et tapez sur 'Entrée' /n L'outil fera le reste et insèrera sur votre bureau le nouveau fichier HTML")

menu()