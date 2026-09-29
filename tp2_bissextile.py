a = float(input("Entrez une année de votre choix"))

#on teste si l'année est divisible par 400 ou bien si elle est divisible par 4 sans l'être par 100

if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0) :
    print("Votre année est bissextile")
else :
    print("Votre année n'est pas bissextile")