# Un attracteur de Lorenz à deux courbes. 
# Résumé
Le programme calcule deux courbes de Lorenz avec des paramètres différents. Dans l'exemple initial, elles ne diffèrent que par les conditions initiales. 
On peut visualiser les deux courbes en 3D dans le fichier ./tranches/lorenz.png.

Les fichiers dans le répertoire ./svg sont faits pour la découpe laser, il n'y a que des découpes (trous+bord). Pour le moment (16/11 à 11h25), il reste
une découpe dans le bas pour les insérer dans un support. 

Je vais l'enlever plus tard pour trouver un système plus pratique. Dites-moi quel style d'attache vous penser utiliser pour fixer les tranches de carton sur un socle. 

Les fichiers dans le répertoire ./tranches contiennent des images où figurent les numéros des trous pour chacune des courbes (couleurs différentes) pour faire le 'relié'

# Le programme
On le lance avec 'run' dans un interprète Python. Si vous le lancez ailleurs que dans un clone du GIT, il faut créer d'abord les répertoires 'svg' et 'tranches'. 
Le programme fabrique alors tous les fichiers svg et png. 

# Paramètres

Pratiquement tous les paramètres accessibles sont au début du programme (à partir de la ligne 16):

1. nbtranches : le nombre de plans sécants (par défaut, 20)
2. dt : L'incrément entre deux points de la courbe. Je n'ai pas experimenté. 
3. RAYON : le rayon des trous pour la découpe. 
4. Ligne 53 : s,r,b : les paramètres de la courbe de Lorenz. Pas expérimenté non plus. 
5. Ligne 81 : Les conditions initiales de la première courbe (bleue)
6. Ligne 86 : Les conditions initiales de la première courbe (rouge-orangé)
