# Ecrivez votre code ici !
nombre = ("1, 2, 3, 4, 5")
print("nombre:", nombre)


#  Utilisation des méthodes split(",")pour transformer cette chaîne de caractères en une variable de type liste `liste`, puis **affichez-la**.
ma_liste = nombre.split(",")
print("ma_liste:", ma_liste)


# conversion de la chaine de caractères en une liste d'entiers avec la fonction int() tout en utilisant la boucle for
ma_liste = [int(i) for i in ma_liste]
print("ma_liste:", ma_liste)

# Utilisation de la fonction sum() pour calculer la somme des éléments de la liste `liste` et **affichez-la**.
somme = sum(ma_liste)
print("somme:", somme)

# Utilisation de la fonction len() pour calculer le nombre d'éléments de la liste `liste` et **affichez-le**.
nombre_elements = len(ma_liste)
print("nombre_elements:", nombre_elements)

#  calculer la moyenne de la liste `liste` et **affichez-le**.
moyenne = somme / nombre_elements
print("moyenne:", moyenne)

# le nombre d'elements superieurs à la moyenne dans la liste `liste` et **affichez-le**.
elements_superieurs = [i for i in ma_liste if i > moyenne]
nombre_superieurs = len(elements_superieurs)
print("nombre_superieurs:", nombre_superieurs)

# le nombre d'éléments pairs dans la liste `liste` et **affichez-le**.
elements_pairs = [i for i in ma_liste if i % 2 == 0]
nombre_pairs = len(elements_pairs)
print("nombre_pairs:", nombre_pairs)

# Utilisation de la fonction max() pour trouver l'élément le plus grand de la liste `liste` et **affichez-le**.
element_max = max(ma_liste)
print("element_max:", element_max)

# Utilisation de la fonction min() pour trouver l'élément le plus petit de la liste `liste` et **affichez-le**.
element_min = min(ma_liste)
print("element_min:", element_min)

# Utilisation de la fonction sorted() pour trier les éléments de la liste `liste` par ordre croissant et **affichez-la**.
liste_triee = sorted(ma_liste)
print("liste_triee:", liste_triee)

# Utilisation de la fonction reversed() pour inverser l'ordre des éléments de la liste `liste` et **affichez-la**.
liste_inversee = reversed(ma_liste)
print("liste_inversee:", list(liste_inversee))

# Utilisation de la fonction list() pour convertir la chaîne de caractères `nombre` en une liste de caractères et **affichez-la**.
liste_caracteres = list(nombre)
print("liste_caracteres:", liste_caracteres)

# Utilisation de la fonction join() pour convertir la liste `liste` en une chaîne de caractères séparée par des virgules et **affichez-la**.
chaine_caracteres = ",".join(map(str, ma_liste))
print("chaine_caracteres:", chaine_caracteres)

# 