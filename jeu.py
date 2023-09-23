import pygame
from pygame.locals import *

pygame.init() # important

# Définition de la surface de rendu (la fenêtre)
display = pygame.display.set_mode((800, 800)) # (largeur, hauteur) de la fenetre

# Chargement et mise à l'échelle de l'image
sprite = pygame.image.load("invader.png") # Chemin relatif au fichier python (possible aussi de mettre le chemin complet)
sprite = pygame.transform.scale(sprite, (130, 100)) # (image, (scale_x, scale_y))

pos_balle = [300, 100] # [x, y]
vel_balle = [0.5, 0.25]

pos_raquette = [100, 100] # [x, y]

points = 0


font = pygame.font.SysFont(None, 70)

last_time = pygame.time.get_ticks()

# Boucle de rendu
end = False
while not end:
	for event in pygame.event.get():
		if event.type == QUIT:
			end = True

	# Mouvement de la raquette

	pressed_keys = pygame.key.get_pressed()
	if pressed_keys[K_DOWN]:
		pos_raquette[1] += 1 * dt
	if pressed_keys[K_UP]:
		pos_raquette[1] -= 1 * dt

	display.fill((50, 100, 250)) # ((rouge, vert, bleu)) entre 0 et 255

	# Physique

	current_time = pygame.time.get_ticks()
	dt = current_time - last_time

	last_time = pygame.time.get_ticks() 

	
	pos_balle[0] += vel_balle[0] * dt
	pos_balle[1] += vel_balle[1] * dt

	if pos_balle[0] + 130 > 800: # Si collision
		pos_balle[0] -= vel_balle[0] * dt
		vel_balle[0] *= -1 # On inverse la vélocité

	if pos_balle[1] + 100 > 800:
		pos_balle[1] -= vel_balle[1] * dt
		vel_balle[1] *= -1
	if pos_balle[1] < 0:
		pos_balle[1] -= vel_balle[1] * dt
		vel_balle[1] *= -1

	# Collision raquette-balle
	if pos_balle[0] < 100 + 20:
		if not (pos_balle[1] + 100  < pos_raquette[1] or pos_balle[1] > pos_raquette[1] + 100) :
			pos_balle[0] -= vel_balle[0] * dt
			vel_balle[0] *= -1
			points += 1



	# Affichage

	display.blit(sprite, pos_balle) # Dessine l'image sur l'écran (image, (pos_x, pos_y)) # Dessin de la balle
	pygame.draw.rect(display, (255, 255, 255), ((pos_raquette[0], pos_raquette[1]), (20, 100))) # (surface, couleur, rectangle = (pos, taille))

	img = font.render(str(points), True, (255, 0, 0))
	display.blit(img, (20, 20))


	pygame.display.update()



pygame.quit() # important