def arithmetic_arranger(problems, show_answers=False):
    # --- 1. VALIDATION DES ERREURS (Ton code était déjà parfait ici) ---
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # --- 2. PRÉPARATION DES "BACS" POUR CHAQUE LIGNE ---
    # J'ai juste renommé la liste pour que ce soit clair et cohérent.
    premiere_ligne = []
    deuxieme_ligne = []
    ligne_de_tirets = []
    ligne_des_reponses = []

    # --- 3. BOUCLE POUR TRAITER CHAQUE PROBLÈME UN PAR UN ---
    for problem in problems:
        # On extrait les pièces
        nombre1, operateur, nombre2 = problem.split()

        # Validation des erreurs (encore une fois, ton code était parfait)
        if operateur not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not (nombre1.isdigit() and nombre2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(nombre1) > 4 or len(nombre2) > 4:
            return  'Error: Numbers cannot be more than four digits.'

        # --- CALCUL DES LARGEURS (La version nettoyée) ---
        longueur_max_nombres = max(len(nombre1), len(nombre2))
        largeur_colonne = longueur_max_nombres + 2

        # --- CONSTRUCTION DES MORCEAUX ---
        piece1 = nombre1.rjust(largeur_colonne)
        piece2 = operateur + " " + nombre2.rjust(longueur_max_nombres)
        piece3 = "-" * largeur_colonne
        
        # On range les morceaux dans les bons bacs
        premiere_ligne.append(piece1)
        deuxieme_ligne.append(piece2)
        ligne_de_tirets.append(piece3)

        # --- CALCUL ET STOCKAGE DE LA RÉPONSE (SI NÉCESSAIRE) ---
        if show_answers:
            if operateur == '+':
                resultat = int(nombre1) + int(nombre2)
            else:
                resultat = int(nombre1) - int(nombre2)
            
            # Correction de la variable : on utilise `str(resultat)` et on le stocke
            reponse_alignee = str(resultat).rjust(largeur_colonne)
            ligne_des_reponses.append(reponse_alignee)

    # --- 4. ASSEMBLAGE FINAL (APRÈS la fin de la boucle) ---
    # Ton indentation était déjà parfaite ici.
    
    ligne_finale_1 = "    ".join(premiere_ligne)
    ligne_finale_2 = "    ".join(deuxieme_ligne)
    ligne_finale_3 = "    ".join(ligne_de_tirets)
    
    arranged_problems = ligne_finale_1 + "\n" + ligne_finale_2 + "\n" + ligne_finale_3

    if show_answers:
        ligne_finale_4 = "    ".join(ligne_des_reponses)
        arranged_problems += "\n" + ligne_finale_4

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 - 49"])}')


