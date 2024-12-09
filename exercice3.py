from itertools import product

# Générer toutes les combinaisons possibles des valeurs des 5 dés
combinations = product(range(1, 7), repeat=5)

# Compter celles qui donnent une somme égale à 20
count = 0
for combo in combinations:
    if sum(combo) == 20:
        count += 1

print(f"Nombre de façons d'obtenir 20 avec 5 dés: {count}")
