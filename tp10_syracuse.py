nb = int(input("Choississez un nombre positif"))

if nb < 0 :
    print("Erreur")

while nb != 1 :
    if nb % 2 == 0 :
        nb = nb // 2
        print(nb)
    else :
        nb = nb * 3 + 1
        print(nb)
