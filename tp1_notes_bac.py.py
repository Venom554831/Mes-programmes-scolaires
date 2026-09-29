# Créé par Célian, le 14/09/2026 en Python 3.7
'''
Afficher "Felicitations !! Vous avez votre bac avec la mention Tres Bien" (pour une note superireure ou egale a 16)
Afficher "Felicitations !! Vous avez votre bac avec la mention Bien" (pour une note comprise entre 14 et 16)
Afficher "Felicitations !! Vous avez votre bac avec la mention Assez Bien" (pour une note comprise entre 12 et 14)
Afficher "Felicitations !! Vous avez votre bac."(pour une note comprise entre 10 et 12)
Afficher "Encore un peu de courage... vous n'avez pas encore votre bac, vous devez passer l'oral."(pour une note comprise entre 8 et 10)
Afficher "Dommage, vous n'avez pas votre bac. Vous ferez mieux la prochaine fois."
'''
a = float(input("Entrez votre note"))

if a >= 16 :
    print("Felicitations !! Vous avez votre bac avec la mention Très Bien")
elif a >= 14 :
    print("Felicitations !! Vous avez votre bac avec la mention Bien")
elif a >= 12 :
    print("Felicitations !! Vous avez votre bac avec la mention Assez Bien")
elif a >= 10 :
    print("Felicitations !! Vous avez votre bac.")
elif a >= 8 :
    print("Encore un peu de courage... vous n'avez pas encore votre bac, vous devez passer l'oral.")
elif a <= 8 :
    print("Dommage, vous n'avez pas votre bac. Vous ferez mieux la prochaine fois.")

