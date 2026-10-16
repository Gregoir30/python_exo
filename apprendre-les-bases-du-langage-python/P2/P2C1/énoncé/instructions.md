# Instructions  

1. **Demandez** à l'utilisateur de fournir **deux nombres** avec la fonction `input()`. Stockez ces valeurs dans `nombre1` et `nombre2`.
2. **Vérifiez** que les deux variables sont bien des nombres entiers avec la méthode `isnumeric()`. Si ce n'est pas le cas, affichez une erreur et quittez le programme à l'aide de `raise SystemExit("Fin du programme")`.
3. **Convertissez** les deux variables en entiers avec la fonction `int()`.
4. **Créez** une variable `operation` et utilisez `input()` pour obtenir l'opération souhaitée par l'utilisateur (`"+"`, `"-"`, `"*"` ou `"/"`).
5. **Vérifiez** que l'opération est valide. Sinon, affichez un message d'erreur et quittez le programme.
6. **Effectuez** le calcul en fonction de la valeur de `operation` (à l'aide des structures conditionnelles `if` / `elif` / `else`) et stockez le résultat dans la variable `resultat`.
7. Attention, il est **impossible** de diviser un nombre par **0**, il faut donc prévoir une structure conditionnelle supplémentaire pour quitter le programme si le deuxième nombre est `0` lors d'une division.
8. **Affichez** le `resultat` arrondi à 2 décimales avec `round()`.

