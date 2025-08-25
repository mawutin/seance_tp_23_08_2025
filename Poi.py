#coding.utf-8
x=int(input("Entrer un nombre entier: "))
if x%2==1 and x<0:
    print("Il s'agit d'un nombre impair négatif")
elif x%2==1 and x>0:
    print("Il s'agit d'un nombre impair positif")
if x%2==0 and x<0:
    print("Il s'agit d'un nombre pair négatif")
elif x%2==0 and x>=0:
    print("Il s'agit d'un nombre pair positif")