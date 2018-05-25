# Utilisation de ce repository

# Docker

Ce repository est à monter dans le docker **Kilodocker** disponible à l'adresse https://hub.docker.com/r/juandres/kilodocker/ .
Utiliser le script fourni pour run le docker et autoriser les affichages graphiques.
Toutes les librairies pour la compilation du code source sont comprises dans le docker.

# Comment compiler pour robots réel

Compiler un fichier .c en .hex (pour robot réel) :
```bash
make hex
```
le fichier .hex sera placé dans le dossier courant.

# Lancer Kilogui 

Pour envoyer les .hex aux kilobots, il faut utiliser l'interface graphique Kilogui : `kilogui`
(pas de message d'erreur si le docker a été lancé avec le script fourni)

# Compiler pour simulateur

Utiliser le Makefile `make mEDEA` puis `./mEDEA`.
Le simulateur se lancera automatiquement.
