# Projets de la Certification "Scientific Computing with Python" de freeCodeCamp

Bienvenue dans mon atelier ! Ce repository contient les 5 projets que j'ai réalisé pour obtenir la certification de freeCodeCamp. Chaque projet représente un défi de logique, d'algorithmique et de résolution de problèmes en Python.

---

## 1. Arithmetic Formatter

Ce premier projet consiste à créer une fonction qui prend une liste de problèmes arithmétiques sous forme de chaînes de caractères et les formate de manière verticale et alignée, comme on le ferait sur une feuille de papier.

### ✅ Compétences démontrées :

*   **Manipulation de chaînes de caractères :** Utilisation avancée de `.split()`, `.join()`, `.rjust()`.
*   **Logique conditionnelle :** Gestion de multiples cas d'erreur (opérateurs, format des nombres, etc.).
*   **Pensée algorithmique :** Conception d'une logique "ligne par ligne" pour construire l'affichage final.
*   **Structures de données :** Utilisation de listes pour stocker et assembler les différentes parties de l'affichage.

➡️ **[Voir le code de l'Arithmetic Formatter](https://github.com/Romaric-DEDJINOU/freecodecamp-python-projects/blob/main/arithmetic_arranger.py)**

## 2. Time Calculator

Ce deuxième projet consiste à créer une fonction qui calcule une heure future en ajoutant une durée à une heure de départ. Le défi principal réside dans la gestion des formats horaires (12h/24h), le passage des jours, et l'affichage conditionnel du jour de la semaine.

### ✅ Compétences démontrées :

*   **Logique de manipulation du temps :** Conception d'un algorithme robuste pour gérer les conversions temporelles complexes sans utiliser de librairies externes.
*   **Maîtrise des opérateurs arithmétiques :** Utilisation intensive de la division entière (`//`) et du modulo (`%`) pour décomposer et recomposer le temps.
*   **Formatage de chaînes de caractères :** Utilisation avancée des f-strings (`:02d`) pour un affichage précis et conditionnel.
*   **Gestion des arguments optionnels** et de la logique conditionnelle (`if day:`).

➡️ **[Voir le code du Time Calculator](https://github.com/Romaric-DEDJINOU/freecodecamp-python-projects/blob/main/time_calculator.py)**

## 3. Budget App

Ce projet a été une introduction intense à la **Programmation Orientée Objet (POO)**. L'objectif était de créer une classe `Category` pour gérer des transactions budgétaires (dépôts, retraits, transferts). Le projet s'est conclu par la création d'une fonction pour visualiser les dépenses sous forme de graphique en barres.

### ✅ Compétences démontrées :

*   **Programmation Orientée Objet (POO) :** Création de classes, utilisation de `__init__` et `self`, définition de méthodes d'instance.
*   **Structures de Données :** Manipulation de listes de dictionnaires pour gérer un registre de transactions.
*   **Logique de Formatage de Chaînes :** Construction d'affichages textuels complexes et alignés.

➡️ **[Voir le code du Budget App](https://github.com/Romaric-DEDJINOU/freecodecamp-python-projects/blob/main/budget_app.py)**

## 4. Polygon Area Calculator

Ce projet est une immersion profonde dans les concepts de la **Programmation Orientée Objet (POO)**, notamment l'héritage. L'objectif était de créer une classe `Rectangle` puis une classe `Square` qui en hérite, tout en s'assurant que les objets conservent une logique géométrique cohérente.

### ✅ Compétences démontrées :

*   **Programmation Orientée Objet (POO) :** Maîtrise de la création de classes, des attributs et des méthodes.
*   **Héritage (`Inheritance`) :** Implémentation d'une classe enfant (`Square`) qui hérite d'une classe parent (`Rectangle`).
*   **Surcharge de Méthodes (`Method Overriding`) :** Redéfinition des méthodes du parent (`set_width`, `__str__`) pour adapter le comportement de l'enfant.
*   **Logique Géométrique :** Traduction de concepts mathématiques (aire, périmètre, diagonale) en code fonctionnel.

➡️ **[Voir le code du Polygon Area Calculator](https://github.com/Romaric-DEDJINOU/freecodecamp-python-projects/blob/main/polygon_area_calculator.py)**

## 5. Probability Calculator

Ce projet final est une synthèse des compétences acquises, mêlant la **Programmation Orientée Objet (POO)** et la **logique algorithmique** pour créer une simulation de probabilités. L'objectif était de modéliser un "chapeau" contenant des billes et de calculer la probabilité d'un tirage spécifique en répétant l'expérience des milliers de fois.

### ✅ Compétences démontrées :

*   **Simulation & Probabilités :** Conception d'un algorithme pour mener une expérience de Monte-Carlo.
*   **POO Avancée :** Utilisation de `__init__` avec des arguments variables (`**kwargs`) et manipulation d'objets.
*   **Bibliothèques Standards :** Utilisation des modules `random` pour le hasard et `copy` pour des simulations propres.
*   **Algorithmique :** Implémentation d'une logique de comptage et de comparaison complexe.

➡️ **[Voir le code du Probability Calculator](https://github.com/Romaric-DEDJINOU/freecodecamp-python-projects/blob/main/probability_calculator.py)**
