# Strategie trois pièces
from random import *
# La probabilité de faire face pour la piece biaisée


# Retourne un triplet o-> face, 1-> pile
# et la quatrième coordonnées est le numéro de la piece biaisee
# Une des pièce est biaisée et renvoie face avec la probabilité p
def tirage():
    global p
    sortie=[]
    #La piece biaisée
    biais=randint(0,2)
    for i in range(3):
        if i==biais :
            k=random()
            if k<=p :
                sortie.append(0)
            else:
                sortie.append(1)
        else :
            k=random()
            if k<0.5:
                sortie.append(0)
            else :
                sortie.append(1)
    sortie.append(biais)
    return sortie



if __name__=="__main__":
    p=0.5
   
    nbtirages=10000
    for j in range(50):
        correct=0
        for i in range(nbtirages) : 
         u=tirage()
         #print(tirage())
         possibilites=[]
         for i in range(3):
             piece=u[i]
             if piece==0 :
               possibilites.append(i)
         #print("les 0 ")
         #print(possibilites)
         if len(possibilites)==0:
             choix=randint(0,2)
         else:
             choix=choice(possibilites)
         if choix==u[-1]:
             correct=correct+1
        print(correct)
        print(nbtirages*(1+6*p)/12)
