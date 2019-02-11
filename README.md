# Markdow-Converter

# Description du convertisseur MD to HTML

Le convertisseur que vous allez utiliser vous permettra de convertir vos fichiers Markdown en fichier HTML facilement.

Cet outil est très simple d'utilisation mais nécessite de connaitre PYTHON pour pouvoir maitriser les différentes étapes.

Il faut avant tout télécharger quelques packages pour que la conversion se passe bien.

Packages:
- Marckdown (pip3 install markdown)
- Marckdown2 (pip3 install markdown2)

Ces packages seront automatiquement intégrés dans votre outil de développement (VS Code, Coda2 ou pour ma part CodeRunner2 sur Mac).

Il suffira simplement au début du code de préciser les packages à importer (ex: Import Marckdown, Import OS, etc...)

D'autres packages peuvent être nécessaire mais Python en intègre déjà beaucoup.

Le code s'éxecute de la manière suivante

# Etape 1

L'utilisateur du convertisseur a le choix entre l'option 1 qui lance le convertisseur et l'option 2 qui correspond à l'aide que j'ai rédigé pour faciliter la compréhension du logiciel.

# Etape 2

Lorsque l'utilisateur lance le convertisseur, la commande suivante s'execute:

__"python -m markdown " + fichier + " > index.html"

Le fichier HTML est alors converti et se trouve dans le même dossier que le fichier Markdown d'origine.
