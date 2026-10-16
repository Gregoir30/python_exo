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