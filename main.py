import time
from utilitaires import lire_csv_colonnes, lire_csv_colonne_numerique
from algorithmes_tri import tri_selection, tri_insertion, tri_fusion, tri_rapide
from algorithmes_recherche import recherche_lineaire, recherche_binaire, recherche_min_max



def recherche_maisons_paris(communes, types, taille):
    nb_trouvees = 0
    comparaisons = 0
    t0 = time.time()


# Fonctions de recherche spécifiques
def recherche_maisons_paris(communes, types, taille):
    nb_trouvees = 0
    comparaisons = 0
    t0 = time.time()
    for i in range(taille):
        comparaisons += 1
        if types[i] == "Maison" and communes[i] == "PARIS":
            nb_trouvees += 1
    t1 = time.time()
    print(f"Recherche linéaire MAISONS PARIS : {t1-t0:.4f}s | {comparaisons} comparaisons | Trouvées: {nb_trouvees}")
    return t1-t0, comparaisons, nb_trouvees


def recherche_appart_3p(types, nb_pieces, taille):
    nb_trouvees = 0
    comparaisons = 0
    t0 = time.time()
    for i in range(taille):
        comparaisons += 1
        if types[i] == "Appartement" and nb_pieces[i] == "3":
            nb_trouvees += 1
    t1 = time.time()
    print(f"Recherche APPART 3P : {t1-t0:.4f}s | {comparaisons} comparaisons | Trouvés: {nb_trouvees}")
    return t1-t0, comparaisons, nb_trouvees


def recherche_binaire_prix(prix_trie, cible):
    gauche = 0
    droite = len(prix_trie) - 1
    comparaisons = 0
    t0 = time.time()
    pos = -1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        comparaisons += 1
        if prix_trie[milieu] == cible:
            pos = milieu
            break
        elif prix_trie[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    t1 = time.time()
    print(f"Recherche binaire PRIX 350000€ : {t1-t0:.4f}s | {comparaisons} comparaisons | Position: {pos}")
    return t1-t0, comparaisons, pos


def recherche_min_max_prixm2(prixm2, taille):
    t0 = time.time()
    minv = float('inf')
    maxv = float('-inf')
    comparaisons = 0
    for i in range(taille):
        try:
            val = float(prixm2[i])
        except ValueError:
            continue
        comparaisons += 1
        if val < minv:
            minv = val
        comparaisons += 1
        if val > maxv:
            maxv = val
    t1 = time.time()
    print(f"Min/Max PRIX_M2 : {t1-t0:.4f}s | {comparaisons} comparaisons | Min: {minv}€/m² | Max: {maxv}€/m²")
    return t1-t0, comparaisons, minv, maxv


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
    # Lecture des colonnes nécessaires
    colonnes = ["prix", "surface", "commune", "type_local", "nb_pieces", "prix_m2"]
    data = lire_csv_colonnes(nom_fichier, colonnes)
    donnees_prix = [float(x) for x in data["prix"] if x]
    donnees_surface = [float(x) for x in data["surface"] if x]
    communes = data["commune"]
    types = data["type_local"]
    nb_pieces = data["nb_pieces"]
    prixm2 = data["prix_m2"]
    if len(donnees_prix) < max(tailles) or len(donnees_surface) < max(tailles):
        print(f"Pas assez de données dans le CSV (prix: {len(donnees_prix)}, surface: {len(donnees_surface)})")
    else:
        tester_tris(donnees_prix, donnees_surface, tailles)
        # RECHERCHES sur 500 et 1000 éléments
        for taille in [500, 1000]:
            print(f"\n=== RECHERCHES SUR {taille} ÉLÉMENTS ===")
            # Maisons à Paris
            recherche_maisons_paris(communes, types, taille)
            # Recherche binaire prix 350000 (sur tableau trié)
            tab_prix = donnees_prix[:taille]
            # Tri préalable obligatoire (tri fusion pour garantir l'ordre)
            tab_prix_trie, _ = tri_fusion(tab_prix)
            recherche_binaire_prix(tab_prix_trie, 350000)
            # Min/Max prix_m2
            recherche_min_max_prixm2(prixm2, taille)
            # Appartements 3 pièces
            recherche_appart_3p(types, nb_pieces, taille)
