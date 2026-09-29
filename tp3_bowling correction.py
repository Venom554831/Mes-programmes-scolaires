lancer1 = int(input("boule 1"))
if lancer1 < 0 or lancer1 > 10 :
    print("!")

if lancer1 == 10 :
    print("X")

else :
    
    lancer2 = int(input("boule 2"))
    total = lancer1 + lancer2
    if lancer2 < 0 or lancer2 > 10  or total > 10 :
        print("!")
    
    elif total == 10 :
        print("/")
    else :
        print("nb de quille :", total)