nombre1 = int(input("Entrez un nombre entier: "))
nombre2 = int(input("Entrez un autre nombre entier: "))

# calcul du quotient et du reste de la division entière
try:
    quotient = nombre1 // nombre2
    reste = nombre1 % nombre2
    print("Le quotient de la division entière de", nombre1, "par", nombre2, "est:", quotient)
    print("Le reste de la division entière de", nombre1, "par", nombre2, "est:", reste)
except ZeroDivisionError:
    print("Erreur: Division par zéro impossible.")
except ValueError:
    print("Erreur: Veuillez entrer des nombres entiers valides.")