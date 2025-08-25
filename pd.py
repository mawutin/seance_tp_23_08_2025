#coding.utf-8
score=0
print("Q1:Qui est le président actuel du Bénin?")
print("a-Patrice TOLON  b-Patrice TALON  C-Paul BIYA")
q1=input("Entrer la lettre correspondante: ")
if q1=="b":
    print("Bravo, +1")
    score=score+1
else:
    print("Mauvaise réponse +0")

print("Q1:En quelle année Bénin a eu son indépedance?")
print("a-1980  b-2018 C-1960")
q2=input("Entrer la lettre correspondante: ")
if q2=="c":
    print("Bravo, +1")
    score=score+1
else:
    print("Mauvaise réponse +0")
print("Q1:YAYI Boni n'a jamais été président au Bénin")
print("a-faux  b-vrai ")
q3=input("Entrer la lettre correspondante: ")
if q3=="a":
    print("Bravo, +1")
    score=score+1
else:
    print("Mauvaise réponse +0")
print("votre score final est :", score)