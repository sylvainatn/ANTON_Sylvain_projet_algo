import time

# Lecture du CSV sans bibliothèque externe
def lire_csv_colonne_numerique(nom_fichier, nom_colonne):
    donnees = []
    with open(nom_fichier, 'r', encoding='utf-8') as f:
        lignes = f.readlines()
        if not lignes:
            return donnees
        en_tete = lignes[0].strip().split(',')
        try:
            idx = en_tete.index(nom_colonne)
        except ValueError:
            raise Exception(f"Colonne '{nom_colonne}' non trouvée dans le CSV.")
        for ligne in lignes[1:]:
            champs = ligne.strip().split(',')
            if len(champs) > idx:
                val = champs[idx].replace(',', '.')
                try:
                    donnees.append(float(val))
                except ValueError:
                    continue
    return donnees


from algorithmes_tri import tri_selection, tri_insertion, tri_fusion, tri_rapide
from algorithmes_recherche import recherche_lineaire, recherche_binaire, recherche_min_max



def tester_tris(donnees_prix, donnees_surface, tailles, fichier_resultats="resultats.txt"):
    tris = [
        ("SÉLECTION", tri_selection),
        ("INSERTION", tri_insertion),
        ("FUSION", tri_fusion),
        ("RAPIDE", tri_rapide)
    ]
    lignes = []
    for taille in tailles:
        lignes.append(f"\n=== TRI PAR PRIX ({taille} éléments) ===\n")
        tab_prix = donnees_prix[:taille]
        for nom, algo in tris:
            t0 = time.time()
            if nom == "FUSION":
                res, nb_comp = algo(tab_prix)
                nb_op = "-"
                ligne = f"Tri {nom} par PRIX : {time.time()-t0:.4f}s | {nb_comp} comparaisons"
            elif nom == "RAPIDE":
                res, nb_comp, nb_ech = algo(tab_prix)
                ligne = f"Tri {nom} par PRIX : {time.time()-t0:.4f}s | {nb_comp} comparaisons | {nb_ech} échanges"
            elif nom == "SÉLECTION":
                res, nb_comp, nb_ech = algo(tab_prix)
                ligne = f"Tri {nom} par PRIX : {time.time()-t0:.4f}s | {nb_comp} comparaisons | {nb_ech} échanges"
            elif nom == "INSERTION":
                res, nb_comp, nb_dec = algo(tab_prix)
                ligne = f"Tri {nom} par PRIX : {time.time()-t0:.4f}s | {nb_comp} comparaisons | {nb_dec} décalages"
            print(ligne)
            lignes.append(ligne + "\n")
        lignes.append(f"\n=== TRI PAR SURFACE ({taille} éléments) ===\n")
        tab_surface = donnees_surface[:taille]
        for nom, algo in tris:
            t0 = time.time()
            if nom == "FUSION":
                res, nb_comp = algo(tab_surface)
                nb_op = "-"
                ligne = f"Tri {nom} par SURFACE : {time.time()-t0:.4f}s | {nb_comp} comparaisons"
            elif nom == "RAPIDE":
                res, nb_comp, nb_ech = algo(tab_surface)
                ligne = f"Tri {nom} par SURFACE : {time.time()-t0:.4f}s | {nb_comp} comparaisons | {nb_ech} échanges"
            elif nom == "SÉLECTION":
                res, nb_comp, nb_ech = algo(tab_surface)
                ligne = f"Tri {nom} par SURFACE : {time.time()-t0:.4f}s | {nb_comp} comparaisons | {nb_ech} échanges"
            elif nom == "INSERTION":
                res, nb_comp, nb_dec = algo(tab_surface)
                ligne = f"Tri {nom} par SURFACE : {time.time()-t0:.4f}s | {nb_comp} comparaisons | {nb_dec} décalages"
            print(ligne)
            lignes.append(ligne + "\n")
    with open(fichier_resultats, "w", encoding="utf-8") as f:
        f.writelines(lignes)

if __name__ == "__main__":
    nom_fichier = "Transactions immobilières.csv"
    tailles = [100, 500, 1000]
    # Lecture des colonnes prix et surface
    donnees_prix = lire_csv_colonne_numerique(nom_fichier, "prix")
    donnees_surface = lire_csv_colonne_numerique(nom_fichier, "surface")
    if len(donnees_prix) < max(tailles) or len(donnees_surface) < max(tailles):
        print(f"Pas assez de données dans le CSV (prix: {len(donnees_prix)}, surface: {len(donnees_surface)})")
    else:
        tester_tris(donnees_prix, donnees_surface, tailles)
