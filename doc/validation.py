# Strategie trois pièces
from random import *
# La probabilité de faire face pour la piece biaisée


# Retourne un triplet o-> face, 1-> pile
# et la quatrième coordonnée est le numéro de la piece biaisee
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

def leopold1(nbtirages):
    # On choisit la première pièce (une pièce au hasard, plutôt), sans regarder le résultat du tirage
    # On n'a rien à faire
    return 1/3*nbtirages

def leopold2(nbtirages):
    # On tire une première pièce. Si elle donne face, on la choisit, sinon
    # on choisit la deuxième
    # Algo : on utilise la fonction tirage() et on applique l'algo
    # p=0.6 correct=0.3667
    correct=0
    for i in range(nbtirages):
        u=tirage()
        if u[0]==0: #la première pièce fait face
            choix=0
        else : choix=1
        if choix==u[3]:
            correct=correct+1
    return correct/nbtirages

def leopold3(nbtirages):
    # Je garde la première pièce qui donne face. Si aucune ne donne face, on choisit la première
    # p=0.6 correct=0.3666
    correct=0
    for i in range(nbtirages):
        u=tirage()
        if u[0]==0 :
            choix=0
        elif u[1]==0:
            choix=1
        elif u[2]==2:
            choix=2
        else:
            choix =1
        if choix==u[3]:
            correct=correct+1
    return correct/nbtirages

def leopold4(nbtirages):
    # Je lance trois fois la première pièce. Si elle donne une majorité de 'face'
    # je dis que c'est elle. Sinon, je choisis une des deux autre pièces au hasard
    # p=0.6 correct: 0.3826
    correct=0
    for i in range(nbtirages): 
        k=random()
        if (k<1/3):
            # On a choisi la pièce biaisée
            # On tire trois fois
            nbfaces=0
            for j in range(3):
                # un tirage de la pièce
                k=random()
                if k<p:
                    nbfaces+=1
            if nbfaces>=2:
                # On la choisit, et on a raison
                correct+=1
            # sinon, on a faux.
        else:
            # On a choisi une pièce non biaisée
            # On tire trois fois
            nbfaces=0
            for j in range(3):
                # un tirage de la pièce
                k=random()
                if k<0.5:
                    nbfaces+=1
            if nbfaces>=2:
                # On la choisit, et on a tort
                correct+=0
            else:
                # on a une chance sur deux de choisir la bonne,
                # une des deux pièces restantes
                k=random() 
                if k>0.5:
                        correct+=1
    return correct/nbtirages

            

if __name__=="__main__":
    p=0.6
    value=(p*p*p+p*p*(1-p)*3)/3+1/6
    # Ma strategie : on tire les trois pièces
    # on choisit au hasard une des pièces qui a fait face.
    # S'il n'y en a pas, on tire une pièce au hasard.
    # Probabilité de deviner juste : (1+6p)/12
    # p=0.6 correct=0.3833
    nbtirages=10000
    for j in range(0):
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
    somme=0
    nbtest=50000
    print(value)
    for i in range(nbtest):
     resu=leopold4(10000)
     somme+=resu
     if i%1000==0 and i!=0:
         print(resu, somme/i)
