# 

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

try:
    def division(a, b):
        return a / b
except ZeroDivisionError:
    print("Erreur: Division par zéro impossible.")
except ValueError:
    print("Erreur: Veuillez entrer des nombres valides.")
