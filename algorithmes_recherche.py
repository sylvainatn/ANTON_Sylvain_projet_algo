def recherche_lineaire(tab, valeur):
    ops = 0
    for i, v in enumerate(tab):
        ops += 1  # comparaison
        if v == valeur:
            return i, ops
    return -1, ops

def recherche_binaire(tab, valeur):
    ops = 0
    gauche = 0
    droite = len(tab) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        ops += 1  # comparaison
        if tab[milieu] == valeur:
            return milieu, ops
        elif tab[milieu] < valeur:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return -1, ops

def recherche_min_max(tab):
    if not tab:
        return None, None, 0
    ops = 0
    min_val = max_val = tab[0]
    for v in tab[1:]:
        ops += 1  # comparaison min
        if v < min_val:
            min_val = v
        ops += 1  # comparaison max
        if v > max_val:
            max_val = v
    return min_val, max_val, ops
