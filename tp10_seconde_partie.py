nb = int(input("Choississez un nombre positif"))
et = 0
maximum = nb
if nb < 0 :
    print("Erreur")

while nb != 1 :
    if nb % 2 == 0 :
        nb = nb // 2
        print(nb)
    else :
        nb = nb * 3 + 1
        print(nb)
    if nb > maximum :
        maximum = nb
    et = et + 1
print("Le nombre d'étape est", et)
print("Votre maximum est", maximum)