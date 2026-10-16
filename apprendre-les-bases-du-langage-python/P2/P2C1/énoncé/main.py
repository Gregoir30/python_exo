# Ecrivez votre code ici !
# calculatrice.py

nombre1 = input("Entrez un nombre entier: ")
nombre2 = input("Entrez un nombre entier: ")

if not nombre1.isnumeric() or not nombre2.isnumeric():
    print("Erreur: les deux nombres doivent être des nombres entiers")
    raise SystemExit("Fin du programme")

nombre1 = int(nombre1)
nombre2 = int(nombre2)

calculate_sign = input("Entrez un opérateur (+, -, *, /, %): ")

if calculate_sign == "+":
    resultat = nombre1 + nombre2
elif calculate_sign == "-":
    resultat = nombre1 - nombre2
elif calculate_sign == "*":
    resultat = nombre1 * nombre2
elif calculate_sign == "/":
    if nombre2 == 0:
        print("Erreur: impossible de diviser par zéro.")
        raise SystemExit("Fin du programme")
    resultat = round(nombre1 / nombre2, 2)
elif calculate_sign == "%":
    if nombre2 == 0:
        print("Erreur: impossible de diviser par zéro.")
        raise SystemExit("Fin du programme")
    resultat = nombre1 % nombre2
else:
    print("Erreur: le symbole d'opération doit être '+', '-', '*', '/' ou '%'.")


# Affiche le résultat
print(f"Le résultat de l'opération est: {resultat}")
