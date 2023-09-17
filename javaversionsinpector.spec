# javaversionsinpector.spec

# Importez les classes Analysis, EXE et COLLECT de PyInstaller
from PyInstaller.utils.hooks import collect_data_files

# Configurez le chemin de l'icône
icon_path = 'icone.ico'

# Ajoutez le chemin de l'icône au collecteur de données
datas = collect_data_files('JavaVersionsInspector', include_py_files=False)

# Configurez les paramètres de PyInstaller
block_cipher = None

a = Analysis(['JavaVersionsInspector.py'],
             pathex=['.'],  # Utilisez le répertoire courant comme chemin
             binaries=[],
             datas=datas,
             )

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='JavaVersionsInspector.exe',  # Nom complet de l'exécutable
          icon=icon_path,  # Spécifiez l'icône
          onefile=True,  # Ajoutez l'option --onefile
          console=True
          )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               upx_exclude=[],
               name='JavaVersionsInspector',  # Nom de vôtre application
               )

# Fin du fichier de spécifications
