"""
Nom du fichier: JavaVersionsInspector.py
Auteur: Chewby
Dates: Crée le 07/09/2023 et mise à jour : 15/09/2023
Description:
Ce script inspecte le disque dur à la recherche des fichiers "java.exe" sur le disque pour déterminer leur version et fournisseur associé.
À la fin de l'analyse est génèré un fichier récapitulatif avec la liste des fichiers "java.exe" et les détails de la version.
"""

import os
import sys
import subprocess
from datetime import datetime


def detecter_fichiers_java(lecteur, fichier_export):
    fichiers_java = []
    compteur = 0  # Initialiser le compteur

    # Parcours récursif du disque spécifié pour trouver les fichiers "java.exe"
    for root, _, files in os.walk(lecteur + ":\\"):
        for filename in files:
            if filename.lower() == "java.exe":
                compteur += 1  # Incrémenter le compteur
                chemin_complet = os.path.join(root, filename)
                fichiers_java.append(chemin_complet)
                print(f"{compteur}. Fichier \"java.exe\" trouvé : {chemin_complet}")
                # Écriture immédiate dans le fichier d'export
                with open(fichier_export, "a", encoding="utf-8") as fichier:
                    fichier.write(f"{compteur}. Fichier \"java.exe\" trouvé : {chemin_complet}\n")

                # Effectuer le traitement immédiatement sur le fichier trouvé
                output = verifier_version_java(chemin_complet)
                print("Détail des informations obtenues avec la commande '-version' :")
                print(output)

                # Écriture immédiate de la sortie de la commande dans le fichier d'export
                with open(fichier_export, "a", encoding="utf-8") as fichier:
                    fichier.write(
                        "Détail des informations obtenues avec la commande '-version' :\n")
                    fichier.write(output + "\n")

    nombre_de_fichiers = len(fichiers_java)
    print(f"Nombre de fichiers \"java.exe\" trouvés : {nombre_de_fichiers}")

    # Exporter le nombre total de fichiers en fin de fichier
    with open(fichier_export, "a", encoding="utf-8") as fichier:
        fichier.write(f"Nombre total de fichiers \"java.exe\" trouvés : {nombre_de_fichiers}\n")

    print(f"Liste exportée dans le fichier {fichier_export}.")

    return fichiers_java


def exporter_fichier(chemins_fichiers, fichier_export):
    with open(fichier_export, "a", encoding="utf-8") as fichier:
        for chemin_fichier in chemins_fichiers:
            fichier.write(chemin_fichier + "\n")
            output = verifier_version_java(chemin_fichier)
            fichier.write("Détail des informations obtenues avec la commande '-version' :\n")
            fichier.write(output + "\n")
        fichier.write(f"Nombre total de fichiers \"java.exe\" trouvés : {len(chemins_fichiers)}\n")


def verifier_version_java(chemin_java):
    try:
        commande = [chemin_java, "-version"]
        result = subprocess.run(commande, capture_output=True, text=True, check=True)
        return result.stderr
    except subprocess.CalledProcessError as e:
        return str(e)


def initialiser_fichier_export():
    date_heure = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nom_fichier = f"export_{date_heure}.txt"
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        fichier.write(f"Liste des fichiers \"java.exe\" exportée le {date_heure} :\n\n")
    return nom_fichier


def main():
    print("JavaVersionsInspector - Version 0.1 - Réalisé par Chewby ;-)")
    print("Inspecte les fichiers \"java.exe\" sur le disque pour déterminer leur version et fournisseur associé.")

    while True:
        lecteur = input(
            "Choisissez un lecteur (par exemple, C, D, etc.) ou tapez 'exit' pour quitter, puis appuyez sur Entrée : ")

        if lecteur.lower() == 'exit':
            print("Merci d'avoir utilisé JavaVersionsInspector.")
            input("Appuyez sur Entrée pour quitter...")
            sys.exit()

        if not os.path.exists(lecteur + ":\\"):
            print("Lecteur spécifié non trouvé.")
            continue

        fichier_export = initialiser_fichier_export()

        print("Recherche en cours, veuillez patienter...\n")

        fichiers_java = detecter_fichiers_java(lecteur, fichier_export)

        if not fichiers_java:
            print("Aucun fichier java.exe trouvé.")

        reponse = input("Voulez-vous refaire une analyse ? (O/N) : ")

        if reponse.lower() != 'o':
            print("Merci d'avoir utilisé JavaVersionsInspector.")
            input("Appuyez sur Entrée pour quitter...")
            sys.exit()


if __name__ == '__main__':
    main()
