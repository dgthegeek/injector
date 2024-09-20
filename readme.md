# Injector Project

## Description

Le projet Injector est un outil de cybersécurité développé dans le cadre d'une formation universitaire. Il permet de fusionner deux programmes binaires en un seul, créant ainsi un exécutable qui lancera à la fois un programme légitime et un programme potentiellement malveillant. Cet outil est conçu uniquement à des fins éducatives et doit être utilisé exclusivement dans un environnement contrôlé par l'université.

## Avertissement

**ATTENTION** : Cet outil est destiné uniquement à des fins éducatives dans le cadre d'une formation en cybersécurité. Son utilisation en dehors d'un environnement contrôlé et autorisé est strictement interdite et peut être illégale.

## Fonctionnalités

- Fusion de deux binaires (un légitime et un potentiellement malveillant) en un seul exécutable.
- Création d'un script Python intermédiaire pour gérer l'exécution des deux binaires.
- Utilisation de PyInstaller pour créer un exécutable autonome.
- Compatible avec macOS (peut nécessiter des ajustements pour d'autres systèmes d'exploitation).

## Fonctionnement détaillé

1. **Création d'un script d'injection** :
   - Le code crée un nouveau script Python qui contient des fonctions pour exécuter les deux binaires originaux.
   - Ce script exécute les binaires séquentiellement, sans capturer leurs outputs.

2. **Utilisation de PyInstaller** :
   - PyInstaller est utilisé pour créer un nouvel exécutable unique.
   - Cet exécutable contient le script d'injection, les deux binaires originaux, et toutes les dépendances nécessaires.

3. **Exécution** :
   - Lorsque l'exécutable final est lancé, il exécute d'abord le binaire malveillant, puis le binaire légitime.
   - Les outputs des binaires s'affichent normalement dans la console ou l'interface graphique.

## Note sur les structures d'exécutables

- Le code utilise une approche de haut niveau et ne manipule pas directement les structures internes des exécutables (comme les Mach-O headers, load commands, etc.).
- PyInstaller gère automatiquement ces aspects complexes.
- Cette approche offre une bonne portabilité et simplicité, mais limite le contrôle fin sur la structure de l'exécutable résultant.

## Prérequis

- Python 3.x
- PyInstaller (`pip install pyinstaller`)

## Installation

1. Clonez ce dépôt ou téléchargez le script `injector.py`.
2. Assurez-vous que Python 3.x est installé sur votre système.
3. Installez PyInstaller en exécutant :
   ```
   pip install pyinstaller
   ```

## Utilisation

1. Exécutez le script `injector.py` :
   ```
   python injector.py
   ```

2. Lorsque vous y êtes invité, entrez le chemin du binaire malveillant.

3. Ensuite, entrez le chemin du binaire légitime.

4. Le script générera un nouvel exécutable fusionné dans le même répertoire que le script.

## Exemple d'utilisation

```
$ python injector.py
Enter your malicious binary path: /path/to/malicious/binary
Enter your legit binary path: /path/to/legitimate/binary
Injected binary generated and saved as: legitimate-injected
```

## Structure du projet

- `injector.py` : Le script principal qui gère le processus d'injection.
- `inject_script.py` : Un script généré temporairement qui est compilé dans l'exécutable final.
- `[nom-du-binaire-légitime]-injected` : L'exécutable final généré.

## Nettoyage

Le script nettoie automatiquement les fichiers temporaires après la génération de l'exécutable final. Cela inclut :
- Suppression du script `inject_script.py`
- Suppression du fichier `.spec` généré par PyInstaller
- Suppression des dossiers `build` et `dist`

## Limitations et perspectives d'amélioration

- Le code actuel ne permet pas un contrôle fin sur la structure de l'exécutable résultant.
- Une approche plus avancée pourrait impliquer l'analyse et la manipulation directes des structures des exécutables, nécessitant l'utilisation de bibliothèques spécialisées.

## Contributions

@dgthegeek