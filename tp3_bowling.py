
print("Bienvenue au bowling !")

score = 0

# Premier lancer
lancer1 = int(input("Combien de quilles au premier lancer ? "))
if lancer1 == 10 :
    print("X")

# Deuxième lancer
lancer2 = int(input("Combien de quilles au deuxième lancer ? "))

# Calcul du score
score = lancer1 + lancer2

print("Votre score est de", score)

# Vérification
if lancer1 + lancer2 == 10:
    print("/")
else:
    print("Bien joué !")

# Deuxième tour
lancer1 = int(input("Combien de quilles au premier lancer du 2e tour ? "))
lancer2 = int(input("Combien de quilles au deuxième lancer du 2e tour ? "))

score = score + lancer1 + lancer2

print("Votre score est maintenant de", score)

print("Partie terminée !")