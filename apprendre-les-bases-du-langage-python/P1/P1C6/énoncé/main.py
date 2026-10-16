# Écrivez votre code ici !
fruit = [ "apple", "banana", "orange", "peach"]

# ajouter un fruit à la liste
fruit.append("mangues")

print(fruit)
print(fruit[0])

# supprimer un fruit de la liste
fruit.remove("banana")
print(fruit)

# modifier le fruit 2 de la liste
print("le fruit 2 de notre liste est :", fruit[1])

fruit[1] = "kiwi"
print(fruit)

# afficher la longueur de la liste
print("la longueur de notre liste est :", len(fruit))

# trier la liste
fruit.sort()
print(fruit)


langage = "Python"
# langage[3] = "v" # Erreur car les chaînes de caractères sont immuables
print(langage[3])
print(langage[0:3]) # affiche les 3 premiers caractères
print(langage[3:]) # affiche à partir du 4ème caractère
print(langage[:3]) # affiche les 3 premiers caractères
print(langage[-1]) # affiche le dernier caractère