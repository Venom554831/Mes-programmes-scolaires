ADN = input("Entrez votre séquence ADN")

for lettre in ADN :
    if not (lettre == "a" or lettre == "t" or lettre == "g" or lettre == "c") :
        print("Erreur dans la séquence")