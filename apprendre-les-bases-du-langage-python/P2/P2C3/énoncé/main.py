# Ecrivez votre code ici

# initialisation d'une fonction
def salaire_mensuel(salaire_annuel):
    salaire_mensuel = salaire_annuel / 12
    return salaire_mensuel

print("Le salaire mensuel pour un salaire annuel de 60000 est:", salaire_mensuel(60000), "euros.")

# initialisation d'une fonction de calcul de salaire hebdomadaire
def salaire_hebdomadaire(salaire_mensuel):
    salaire_hebdomadaire = salaire_mensuel / 4.33
    return salaire_hebdomadaire

salaire_mensuel1 = 40000
print("Le salaire hebdomadaire pour un salaire mensuel de", salaire_mensuel1, "euros est:", salaire_hebdomadaire(salaire_mensuel1), "euros.")



# initialisation d'une fonction de calcul de salaire horaire
def salaire_horaire(salaire_hebdomadaire , heures_travail):
    salaire_horaire = salaire_hebdomadaire / heures_travail
    return salaire_horaire


heures_travail1 = 40
print("Le salaire horaire pour un salaire hebdomadaire de", salaire_hebdomadaire(salaire_mensuel1), "euros et", heures_travail1, "heures de travail est:", salaire_horaire(salaire_hebdomadaire(salaire_mensuel1), heures_travail1), "euros.")


# l'utilisateur doit entrer son salaire annuel

salaire_annuel_input = float(input("Entrez votre salaire annuel: "))


# l'utilisateur doit entrer son volume d'heure de travail par semaine
heures_travail_input = float(input("Entrez votre volume d'heure de travail par semaine: "))

# calcul du salaire mensuel, hebdomadaire et horaire en utilisant les fonctions définies précédemment

salaire_mensuel_input = salaire_mensuel(salaire_annuel_input)
salaire_hebdomadaire_input = salaire_hebdomadaire(salaire_mensuel_input)
salaire_horaire_input = salaire_horaire(salaire_hebdomadaire_input, heures_travail_input)

# affichage des résultats

print("Le salaire hebdomadaire est de:", salaire_hebdomadaire_input, "euros.")
print("Le salaire mensuel est de:", salaire_mensuel_input, "euros.")
print("Le salaire horaire est de:", salaire_horaire_input, "euros.")