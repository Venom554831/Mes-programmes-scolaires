for i in range(1, 21):
    ans = i
    et = 0
    maximum = ans
    while ans != 1:
        if ans % 2 == 0:
            ans = ans // 2
        else :
            ans = ans * 3 + 1
        if ans > maximum:
            maximum = ans
        et = et + 1
        
    print("Le nombre d'étape pour la valeur", i, "est", et)
    print("Le maximum atteint est", maximum)
