#16 novembre 2025
# dessiner deux courbes de Lorenz, avec des conditions initiales différentes
# et les infos pour les réaliser en vrai.

import numpy as np

from math import *
import matplotlib.pyplot as plt
fig = plt.figure()
from mpl_toolkits.mplot3d import Axes3D # <--- This is important for 3d plotting 





# Paramètres de contrôle
# Il y a 3 paramètres de contrôle dans la définition de la fonction de Lorenz (s,r,b) je ne sais pas à quoi ils correspondent. 
# Nombre de plans de coupe
nbtranches=20

# Nombre de points de chaque courbe
num_steps = 1000

# Incrément entre deux points de la courbe
dt = 0.01

# Diamètre des trous. 
RAYON=5 


minx=1000
minz=1000
maxx=-1000
maxz=-1000
minspan=1000
maxspan=-1000
ordre=0
ordre2=0

debut=-15
fin=22

# Les deux listes qui stockent les positions des trous de passage dans les plans pour chaque courbe. 
traces=[[] for i in range(nbtranches)]
traces2=[[] for i in range(nbtranches)]

dernier=0
indice=-1


# La fonction de Lorenz, avec ses conditions initiales
# C'est pas moi qui l'ai écrite
def lorenz(xyz, *, s=10, r=28, b=2.667):
    global minx,minz,maxx,maxz,ordre,dernier,indice
    """
    Parameters
    ----------
    xyz : array-like, shape (3,)
       Point of interest in three-dimensional space.
    s, r, b : float
       Parameters defining the Lorenz attractor.

    Returns
    -------
    xyz_dot : array, shape (3,)
       Values of the Lorenz attractor's partial derivatives at *xyz*.
    """
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
   
    return np.array([x_dot, y_dot, z_dot])





# Une liste pour stocker les points de la courbe
xyzs = np.empty((num_steps + 1, 3))  # Need one more for the initial values
xyzs[0] = (3., 2., 1.05)  # Set initial values

# Pareil pour la deuxième courbe
xyzs2 = np.empty((num_steps + 1, 3))  # Need one more for the initial values
# On a changé les conditions initiales
xyzs2[0] = (20,20,20)  # Set initial values

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt
    xyzs2[i + 1] = xyzs2[i] + lorenz(xyzs2[i]) * dt

    # On ne garde que les points où on passe d'un cote à l'autre d'une plaque
    passage=False
   
    for j in range(nbtranches-1):
        if passage:
            break
        x0=debut+j*(fin-debut)/nbtranches
        if (xyzs[i+1][0]>x0 and xyzs[i][0]<x0) or (xyzs[i+1][0]<x0 and xyzs[i][0]>x0):
          traces[j].append((xyzs[i+1][1],xyzs[i+1][2],ordre))
          ordre=ordre+1
          passage=True
        
    
      
    if xyzs[i+1][1]<minx:
        minx=xyzs[i+1][1]
    if xyzs[i+1][1]>maxx:
        maxx=xyzs[i+1][1]
    if xyzs[i+1][2]<minz:
        minz=xyzs[i+1][2]
    if xyzs[i+1][2]>maxz:
        maxz=xyzs[i+1][2]
    if xyzs[i+1][0]<minspan:
        minspan=xyzs[i+1][0]
    if xyzs[i+1][0]>maxspan:
        maxspan=xyzs[i+1][0]

  # Pareil pour la deuxième courbe. J'aurai pu optimiser mais non
    passage2=False
    for j in range(nbtranches-1):
        if passage2:
            break
        x0=debut+j*(fin-debut)/nbtranches
        if (xyzs2[i+1][0]>x0 and xyzs2[i][0]<x0) or (xyzs2[i+1][0]<x0 and xyzs2[i][0]>x0):
          traces2[j].append((xyzs2[i+1][1],xyzs2[i+1][2],ordre2))
          ordre2=ordre2+1
          passage2=True
        
    
      
    if xyzs2[i+1][1]<minx:
        minx=xyzs2[i+1][1]
    if xyzs2[i+1][1]>maxx:
        maxx=xyzs2[i+1][1]
    if xyzs2[i+1][2]<minz:
        minz=xyzs2[i+1][2]
    if xyzs2[i+1][2]>maxz:
        maxz=xyzs2[i+1][2]
    if xyzs2[i+1][0]<minspan:
        minspan=xyzs2[i+1][0]
    if xyzs2[i+1][0]>maxspan:
        maxspan=xyzs2[i+1][0]
    
   
           
           
# Plot   Affichage de la courbe qui donne une vue globale.
# Les deux courbes avec des couleurs différentes. 


ax = plt.axes(projection='3d')

ax.plot(*xyzs.T, lw=0.5)
ax.plot(*xyzs2.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")



plt.savefig('tranches/lorenz.png')


total=0
total2=0
for i in range(nbtranches):
    total=total+len(traces[i])
    total2=total2+len(traces2[i])
   
# Seul affichage du programme : le nombre de trous pour chaque courbe. 
print("---->",total, "--->",total2)
plt.close('all')
plt.rcParams['figure.figsize'] = [20, 20]
# plot
for j in range(nbtranches):
    
    fig, ax = plt.subplots()
    plt.xlim([minx, maxx])
    plt.ylim([minz, maxz])
  
    ax.set_title(str(debut+j/nbtranches*(fin-debut)))
    ax.scatter([k[0] for k in traces[j]],[k[1] for k in traces[j]] )
    ax.scatter([k[0] for k in traces2[j]],[k[1] for k in traces2[j]] )
    for i in range(len(traces[j])):
     ax.annotate(str(traces[j][i][2]),traces[j][i][0:2])
    for i in range(len(traces2[j])):
     ax.annotate(str(traces2[j][i][2]),traces2[j][i][0:2])



    if j<0:
        rajout="m"+str(abs(j))
    else:
        rajout=str(j)
    plt.savefig('tranches/trace'+rajout+'.png')
    plt.close('all')


# sortie fichiers SVG, un par tranche
# Les points de la première courbe sont en bleu, ceux de la deuxième courbe en rouge.
# Les mêmes couleurs que dans les images qui montrent les numéros d'ordre des points de chaque courbe.

TAILLE=1000 # le coté du carré de l'écran
HAUTEUR=200 # Hauteur du socle
EPAISSEUR=100 # largeur du trou de l'encoche
ESPACE=10 # espace autour du cadre


# Utilitaires SVG
ENTETE="<svg viewBox=\"0 0 "+str(TAILLE+2*ESPACE)+" "+str(TAILLE+2*ESPACE)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
PIED="</svg>\n"

def cercle(cx,cy,rayon=RAYON,couleur="blue"):
    return "<circle cx=\""+str(cx)+"\" cy=\""+str(cy)+"\"  r=\""+str(rayon)+"\"  fill=\"none\" stroke=\""+couleur+"\"/>\n"

def cadre(c=TAILLE,h=HAUTEUR,e=EPAISSEUR):
    s="<polygon points=\""+str(ESPACE)+","+str(ESPACE)+" "+str(c+ESPACE)+","+str(ESPACE)+" "+str(c+ESPACE)+","+str(c+h+ESPACE)+" "+str(ESPACE)+","+str(c+h+ESPACE)+" "+str(ESPACE)+","+str(c+e+ESPACE)+" "+str(c//2+ESPACE)+","+str(c+e+ESPACE)+" "+str(ESPACE+c//2)+","+str(c+ESPACE)+" "+str(ESPACE)+","+str(ESPACE+c)+"\" fill=\"none\"  stroke=\"lime\" />"
    return s



def decoupe():
 
 for numtranche in range(nbtranches):
     image=open("svg/sortie"+str(numtranche)+".svg","w")
     image.write(ENTETE)
     image.write(cadre())
     # Première courbe
     for point in traces[numtranche]:
         cx=ESPACE+TAILLE*(point[0]-minx)/(maxx-minx)
         cy=TAILLE+ESPACE-TAILLE*(point[1]-minz)/(maxz-minz)
         image.write(cercle(cx,cy))
     # Deuxième courbe 
     for point in traces2[numtranche]:
         cx=ESPACE+TAILLE*(point[0]-minx)/(maxx-minx)
         cy=TAILLE+ESPACE-TAILLE*(point[1]-minz)/(maxz-minz)
         image.write(cercle(cx,cy,couleur="red"))
     image.write("<text x=\" "+str(20+ESPACE+TAILLE//2)+"\" y=\" "+str(ESPACE+TAILLE+EPAISSEUR)+"\" fill=\"none\" font-size=\"2em\" stroke=\"red\" >"+str(numtranche)+"</text>\n")
     image.write(PIED)
     image.close()
 


                                                                                                                              

decoupe()
print(minspan," ",maxspan)
  
