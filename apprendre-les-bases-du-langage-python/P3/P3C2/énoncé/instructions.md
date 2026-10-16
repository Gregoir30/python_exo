# Instructions  

À l'aide du package `BeautifulSoup` (`bs4`), extrayez et transformez les informations suivantes à partir du fichier `index.html` :

1. **Ouvrez** et **analysez** le fichier `index.html` avec `BeautifulSoup`.
2. **Extrayez** et **affichez** le titre de la page (`<title>`).
3. **Extrayez** et **affichez** le texte de la balise `<h1>`.
4. **Extrayez** les noms (`<h2>`), les prix (`<p class="price">`) et les descriptions (dernier `<p>`) de tous les produits (`<li>`) de la liste, et stockez-les dans un dictionnaire `all_products`.
5. **Affichez** les informations extraites des produits.
6. **Convertissez** les prix en euros (`€`) en dollars (`$`) avec un taux de conversion de `1.2` (`prix * 1.2`), et ajoutez cette valeur sous la clé `"prix_dollar"` pour chaque produit.
7. **Affichez** le dictionnaire final contenant tous les produits avec leurs prix en dollars.

