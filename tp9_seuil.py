'''
# Programme faux 
a = 2
b = 0
while a**b < 10000 :
    b = b + 1
    if a**b == 8192 :
        print(a**b)
        break
    else:
        continue
'''
n = 0
while 2**(n+1) < 10000 :
    n = n + 1
print("la plus grande puissance est", n)
