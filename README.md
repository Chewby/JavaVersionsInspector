# JavaVersionsInspector

Permet de récupérer les informations des versions "java.exe" sur vos disques dures et d'en faire un export vers un fichier récapitulatif.

### Installation des dépendances

Il n'y a pas d'installation additionnelle.

### Création de l'éxécutable pour le système d'exploitation Windows

Installation de PyInstaller

``` bash
pip install PyInstaller
```
  
Création du package

``` bash
pyinstaller --noconfirm .\javaversionsinpector.spec
```
