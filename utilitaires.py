import time

# Lecture de plusieurs colonnes du CSV sans bibliothèque externe
def lire_csv_colonnes(nom_fichier, colonnes):
   resultats = {col: [] for col in colonnes}
   with open(nom_fichier, 'r', encoding='utf-8') as f:
      lignes = f.readlines()
      if not lignes:
         return resultats
      en_tete = lignes[0].strip().split(',')
      indices = []
      for col in colonnes:
         try:
               indices.append(en_tete.index(col))
         except ValueError:
               raise Exception(f"Colonne '{col}' non trouvée dans le CSV.")
      for ligne in lignes[1:]:
         champs = ligne.strip().split(',')
         for i, col in enumerate(colonnes):
               if len(champs) > indices[i]:
                  val = champs[indices[i]].replace(',', '.')
                  resultats[col].append(val)
               else:
                  resultats[col].append("")
   return resultats


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


def mesure_temps(fonction, *args, **kwargs):
   t0 = time.time()
   res = fonction(*args, **kwargs)
   t1 = time.time()
   return t1-t0, res
