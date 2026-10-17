
# Importation de la fonction get de requests
from requests import get

# Point d'entrée du programme
if __name__ == "__main__":
    # Envoi d'une requête HTTP GET à Google
    response = get("https://google.com")

    # Affichage du code de statut HTTP
    print(response.status_code)

    # Affichage du contenu HTML reçu
    print(response.text)

    # Tentative de lecture de la réponse au format JSON
    print(response.json())

    # Affichage de tous les en-têtes HTTP
    print(response.headers)

    # Affichage du type de contenu retourné
    print(response.headers.get("Content-Type", "Aucun en-tête Content-Type trouvé."))

    # Affichage de la date de la réponse
    print(response.headers.get("Date", "Aucun en-tête Date trouvé."))

    # Affichage du contenu reçu sous forme d'octets
    print(response.content)

    # Affichage du serveur ayant répondu, si cet en-tête existe
    print(response.headers.get("Server", "Aucun en-tête Server trouvé."))

    # Affichage de la limite de requêtes, si cet en-tête existe
    print(response.headers.get("X-RateLimit-Limit", "Aucun en-tête X-RateLimit-Limit trouvé."))

    # Affichage des requêtes restantes, si cet en-tête existe
    print(response.headers.get("X-RateLimit-Remaining", "Aucun en-tête X-RateLimit-Remaining trouvé."))

    # Affichage de l'heure de réinitialisation de la limite, si disponible
    print(response.headers.get("X-RateLimit-Reset", "Aucun en-tête X-RateLimit-Reset trouvé."))
