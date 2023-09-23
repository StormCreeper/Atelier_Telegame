# Atelier_Telegame
Ce dépôt contiendra les fichiers des ateliers Pygame. Je vais y mettre des bouts de code et des explication pour les concepts basiques d'un jeu vidéo.

Utilisation: `python jeu.py`

## Atelier du vendredi 22 septembre 2023
> Premier atelier sur Pygame. Nous avons vu comment ouvrir une fenêtre Pygame, créer la boucle de rendu, dessiner une image à l'écran et la faire bouger à l'aide du clavier.

### Squelette d'un jeu avec Pygame (hésitez pas à le copier-coller et à le remplir)
```python
import pygame
from pygame.locals import *

pygame.init() # important

display = pygame.display.set_mode((800, 800)) # crée une surface pour la fenêtre (largeur, hauteur) de la fenetre

last_time = pygame.time.get_ticks() # Pour le comptage du temps (get_ticks() renvoie le temps actuel en millisecondes)

# Boucle de rendu
end = False
while not end:
	for event in pygame.event.get():
		if event.type == QUIT: # vrai quand l'utilisateur essaye de fermer la fenêtre
			end = True

	display.fill((50, 100, 250)) # remplit l'écran avec la couleur ((rouge, vert, bleu)) (entre 0 et 255)

	current_time = pygame.time.get_ticks() 
	dt = (current_time - last_time) / 1000.0 # dt = temps écoulé depuis la dernière frame en secondes

	last_time = pygame.time.get_ticks() # ne pas oublier de réinitialiser le chronomètre

	pressed_keys = pygame.key.get_pressed()
	# Ici se fera le traitement des entrées clavier

	# Ici se fera le calcul de la physique du jeu

	# Ici se fera le dessin de la scène

	pygame.display.update() # Mise à jour de l'affichage 

pygame.quit() # important
```
### Fonction utiles
#### Affichage
- Pour dessiner un rectangle à l'écran
```python
pygame.draw.rect(display, (rouge, vert, bleu), ((pos_x, pos_y), (largeur, hauteur))) # rouge, vert, bleu ∈ [0, 255], et pos_x, pos_y : coin en haut-gauche du rectangle
```
- Pour charger et dessiner une image à l'écran
```python
# Au début du programme
sprite = pygame.image.load("chemin_vers_l'image") # Charge l'image dans la variable sprite
sprite = pygame.transform.scale(sprite, (largeur, longueur)) # Pour redimensionner l'image

# Dans la boucle de rendu
display.blit(sprite, (pos_x, pos_y)) # affiche l'image à la position souhaitée
```
- Pour afficher du texte
```python
# Au début du programme
font = pygame.font.SysFont(None, taille) # Charge la police par défaut dans font

# Dans la boucle de rendu
text = font.render("texte", True, (rouge, vert, bleu))
display.blit(text, (20, 20))
```
#### Physique
- pour mettre à jour les vitesses et les positions
```python
vel += acc * dt
pos += vel * dt
# Si pos, vel et acc sont des tableaux, décomposer le calcul sur leurs composantes
```













