# Utilisation de ce repository

#Docker

Ce repository est à monter dans le docker **Kilodocker** disponible à l'adresse https://hub.docker.com/r/juandres/kilodocker/ .
Utiliser le script fourni pour run le docker et autoriser les affichages graphiques.
Toutes les librairies pour la compilation du code source est compris dans le docker.

#Comment compiler

Pour compiler un fichier .c, lancer le script compileCode.sh avec le nom du fichier sans son extension
Exemple:
```bash
./compileCode.sh test
```
Les fichier .hex issus de la compilation seront placé dans un dossier build.

#Lancer Kilogui

Pour envoyer les .hex aux kilobots, il faut utiliser l'interface graphique Kilogui : `kilogui`
(pas de message d'erreur si le docker a été lancé avec le script fourni)
