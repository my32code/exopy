nom = "ADILEHOU"
prenom = "Morgan"


# Factorielle avec une boucle for
n = int(input("Entrez un nombre: ")) # Remplacez par le nombre prédéfini
factorielle_for = 1
for i in range(1, n + 1):
    factorielle_for *= i
    print(f"Factorielle de {n} avec for: {factorielle_for}")
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i}: {nom} {prenom}")
        elif i % 3 == 0:
            print(f"{i}: {nom}")
        elif i % 5 == 0:
            print(f"{i}: {prenom}")
        else:
            print(i)
       
    

# Factorielle avec une boucle while
factorielle_while = 1
i = 1
while i <= n:
    factorielle_while *= i
    i += 1
    print(f"Factorielle de {n} avec while: {factorielle_for}")
    while i <= 50:
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i}: {nom} {prenom}")
        elif i % 3 == 0:
            print(f"{i}: {nom}")
        elif i % 5 == 0:
            print(f"{i}: {prenom}")
        else:
            print(i)
        i += 1