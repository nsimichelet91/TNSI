# TP : balles rebondissantes

![image](data/balles1.png){: .center witdh=40%}

## 1. Prise en main de Pygame

```python linenums='1'
import pygame, sys
import time
from pygame.locals import *

LARGEUR = 640
HAUTEUR = 480

pygame.display.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
fenetre.fill([0,0,0])

x = 300
y = 200
dx = 4
dy = -3
couleur = (45,170,250)
rayon = 10

while True :
    fenetre.fill([0,0,0])
    pygame.draw.circle(fenetre,couleur,(x,y), rayon)
    
    x += dx
    y += dy
    
    pygame.display.update()
    
    # routine pour pouvoir fermer «proprement» la fenêtre Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    
    
    time.sleep(0.02)
```

### 1.1  Rajout d'un rebond sur les parois
Modifiez le code précédent afin que la balle rebondisse sur chaque paroi (il suffit de modifier intelligemment les variables de vitesse ```dx``` et ```dy```).


### 1.2 Rajout d'une deuxième balle
Attention au nommage des variables...


### 1.3 Gestion de la collision entre les deux balles
1. À l'aide d'un schéma (papier-crayon !), mettez en évidence le test devant être réalisé pour détecter une collision.
2. Implémentez ce test et affichez "collision" en console lorsque les deux balles se touchent.


Q3. Pour l'illusion du rebond, échangez les valeurs respectives de ```dx``` et ```dy``` pour les deux balles.

### 1.4 Rajout d'une troisième balle et gestion du rebond avec les deux autres.
... vraiment ? Peut-on continuer comme précédemment ?

## 2. La POO à la rescousse : création d'une classe Balle

### 2.1 la classe Balle
L'objectif est que la méthode constructeur dote chaque nouvelle balle de valeurs aléatoires : abscisse, ordonnée, vitesses, couleur, rayon ...  

- Pour l'aléatoire, on pourra utiliser ```randint(a, b)``` qui renvoie un nombre pseudo-aléatoire entre ```a``` et ```b```.
Il faut pour cela importer la fonction, par ```from random import randint``` 

- Vous pouvez aussi doter votre classe ```Balle``` d'une méthode ```dessine``` (qui affiche la balle), d'une méthode ```bouge``` qui la fait bouger, d'une méthode ```rebond``` qui gère les rebonds de la balle sur les murs et d'une méthode ```distance_avec_balle``` qui renvoie la distance entre la balle elle-même et une autre balle. 

Créez cette classe et instanciez une balle.

### 2.2 Plusieurs balles

L'idée est de stocker dans une liste ```sac_a_balles``` un nombre déterminé de balles... 

### 2.3 Collision de toutes les balles

La gestion des collisions entre toutes les balles est la responsabilité du programme qui gère l'ensemble des balles.
Il faut donc écrire une fonction (**PAS UNE METHODE**) pour tester les collisions de toutes les balles du ```sac_a_balles```. Il faut faire en sorte que chaque paire ne soit testée qu'une seule fois.

## 3. Extensions

- Vous pouvez créer des balles de couleurs identiques, sauf une. Cette balle diffusera sa couleur à toutes les balles avec qui elle rentrera en collision.
- En la supprimant de la liste ```sac_a_balles```, vous pouvez faire disparaitre une balle.
- Vous pouvez créer une balle que vous déplacerez au clavier (voir [ici](https://nsimichelet91.github.io/1NSI/T7_Pygame/Initiation_Pygame/){. target="_blank"} pour la gestion des déplacements)
- ...
- Ce que je ne veux pas voir :
  
![](data/paste_chtgpt.png){: .center width=40%}  

## 4. Organisation du projet

!!! tip "Calendrier du projet"
    - 22/09/2026 : démarrage du projet
    - remise du projet sur Capytale : **jeudi 5/11/2026 dernier délai**

!!! Capytale 
    "Dépôt de projet sur Capytale : [notebook](https://capytale2.ac-paris.fr/web/c/0d5d-6963432){:target="_blank"}
    Servez-vous de cette feuille de projet pour y déposer les différentes versions de votre travail.  
    Je pourrai ainsi le consulter au fur et à mesure de votre progression.  

!!! abstract "Évaluation du projet"
    - sur 10 points : note globale du projet.
    - sur 10 points : entretien individuel autour du code du projet. 

