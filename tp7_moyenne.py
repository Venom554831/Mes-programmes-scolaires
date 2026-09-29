n = int(input("Entrez le nombre de notes"))
compteur = 0

for _ in range(n):
    note = float(input("Entrez votre note"))
    compteur = note + compteur
    print(compteur)
compteur = compteur / n
print("Votre moyenne est de", compteur)