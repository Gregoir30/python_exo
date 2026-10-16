# Écrivez votre code ici !
fruit = { 
    "pomme": "rouge",
    "banane": "jaune",
    "orange": "orange"
         }
print(fruit["pomme"])

# ajouter un fruit à la liste
fruit.update({"mangue": "jaune"})
print(fruit)

#  acceder à la couleur d'un fruit
print(fruit["banane"])

couleurbanane = fruit.get("banane")
print(couleurbanane)

# modifier la couleur d'un fruit
fruit["pomme"] = "vert"
print(fruit["pomme"])

# supprimer un fruit de la liste
del fruit["orange"]


# afficher la liste des fruits
print(fruit)

# Méthodes de dictionnaire
# keys() : retourne une liste des clés du dictionnaire
print(fruit.keys())

# values() : retourne une liste des valeurs du dictionnaire
print(fruit.values())

# items() : retourne une liste des tuples (clé, valeur) du dictionnaire
print(fruit.items())

# pop() : supprime un élément du dictionnaire en fonction de sa clé
fruit.pop("banane", None)  # supprime la clé "banane" si elle existe, sinon ne fait rien

# afficher tout le dictionnaire
print(fruit)

# clear() : supprime tous les éléments du dictionnaire
fruit.clear()

