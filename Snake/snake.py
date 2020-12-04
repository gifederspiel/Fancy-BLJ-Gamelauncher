import sys
import pygame
import numpy as np

partikel = 25
schlange = [[13, 13], [13, 14]]
apfelCoords = []
richtung = 0

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([700, 700])

def zeichner():
	screen.fill((0, 102, 0))

	for a in apfelCoords:
		Coords = [a[0]*partikel,a[1]*partikel]
		pygame.draw.rect(screen, (255,0,0), (Coords[0],Coords[1], partikel, partikel), 0)

	kopf = True
	for x in schlange:
		coords = [x[0] * partikel, x[1] * partikel]
		if kopf:
			pygame.draw.rect(screen, (0, 0, 0), (coords[0], coords[1], partikel, partikel), 0)
			kopf = False
		else:
			pygame.draw.rect(screen, (47, 79, 79), (coords[0], coords[1], partikel, partikel), 0)

def apfelCoordGen():
	notOK = True
	while notOK:
		Coord = [np.random.randint(0,28),np.random.randint(0,28)]
		change = False
		for x in schlange:
			if Coord == x:
				change = True
		for x in apfelCoords:
			if Coord == x:
				change = True
		if change == False:
			return Coord
apfelCoords.append(apfelCoordGen())

go = True
anhang = None
apfelInd = -1
ende = False
score = 0

#Richtunen:
	#1=Rechts, 3=Links, 0=Oben, 2=Unten

while go:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and richtung != 2:
				richtung = 0
			if event.key == pygame.K_RIGHT and richtung != 3:
				richtung = 1
			if event.key == pygame.K_DOWN and richtung != 0:
				richtung = 2
			if event.key == pygame.K_LEFT and richtung != 1:
				richtung = 3
	if anhang != None:
		schlange.append(anhang.copy())
		anhang = None
		apfelCoords.pop(apfelInd)

	zahl = len(schlange)-1
	for i in range(1,len(schlange)):
		schlange[zahl] = schlange[zahl-1].copy()
		zahl -= 1

	if richtung == 0:
		schlange [0][1] -= 1
	if richtung == 1:
		schlange [0][0] += 1
	if richtung == 2:
		schlange [0][1] += 1
	if richtung == 3:
		schlange [0][0] -= 1

	for x in range(0,len(apfelCoords)):
		if apfelCoords[x] == schlange[0]:
			anhang = schlange[-1].copy()
			apfelInd = x
			score += 10
	zufall = np.random.randint(0,100)
	if zufall <= 1 and len(apfelCoords) < 4 or len(apfelCoords) == 0:
		apfelCoords.append(apfelCoordGen())

	if not ende != False:
		zeichner()
		pygame.display.update()
	else:
		print("Du hast " + str(score) + " Punkte erreicht")
		sys.exit()
	clock.tick(10)