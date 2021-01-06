import pygame
import sys
import numpy as np
import time
import tkinter as tk
from tkinter import *
import mysql.connector

 
partikel = 25
schlange = [[13,13],[13,14]]
apfelCoords = []
richtung = 0
 
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont('arialblack',24)
screen = pygame.display.set_mode([700,700])
fontBig = pygame.font.SysFont('arialblack',40,)


def countdown():
	zeichner()
	textGrund,textKasten = textObjekt("3",font)
	textKasten.center = ((350,265))
	screen.blit(textGrund,textKasten)
	pygame.display.update()
	time.sleep(1)
	zeichner()
	textGrund,textKasten = textObjekt("2",font)
	textKasten.center = ((350,265))
	screen.blit(textGrund,textKasten)
	pygame.display.update()
	time.sleep(1)
	zeichner()
	textGrund,textKasten = textObjekt("1",font)
	textKasten.center = ((350,265))
	screen.blit(textGrund,textKasten)
	pygame.display.update()
	time.sleep(1)
	zeichner()
	textGrund,textKasten = textObjekt("0",font)
	textKasten.center = ((350,265))
	screen.blit(textGrund,textKasten)
	pygame.display.update()

def textObjekt(text, font):
    textFlaeche = font.render(text, True, (255,255,255))
    return textFlaeche, textFlaeche.get_rect()
 
def zeichner():
    screen.fill((0,102,0))
 
    for a in apfelCoords:
        Coords = [a[0]*partikel,a[1]*partikel]
        pygame.draw.rect(screen, (255,0,0), (Coords[0],Coords[1],partikel,partikel), 0)
 
    kopf = True
    for x in schlange:
        Coords = [x[0] * partikel, x[1] * partikel]
        #Zeichnet Kopf
        if kopf:
            pygame.draw.rect(screen, (0,0,205), (Coords[0],Coords[1],partikel,partikel), 0)
            kopf = False
        else:
            pygame.draw.rect(screen, (0,0,255), (Coords[0],Coords[1],partikel,partikel), 0)
 
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

#Blacklist
blacklist = ["kkk", "bruh", "cringe", "bloat", "holdup", "rape", "livio"]

#Formular für Spielername
user_text= ''
entered = False
active = True

input_rect = pygame.Rect(265,200,140,32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive
i = 1

if i == 1:
	while entered == False:  
  
  
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if input_rect.collidepoint(event.pos):
					active = True
				else:
					active = False

			if event.type == pygame.KEYDOWN:
				if active == True:
					
					#Falls Entertaste gedrück sende Name ab und lade Spiel
					if event.key == pygame.K_RETURN and user_text != '':
						active = False
						for word in blacklist:
							if user_text == word:
								zeichner()
								textGrund,textKasten = textObjekt("Dein Name ist nicht zugelassen",font)
								textKasten.center = ((350,40))
								screen.blit(textGrund,textKasten)
								pygame.display.update()
								time.sleep(1)
								entered = False
								break
								
							else:
								entered = True
								name = user_text

					#Eingabe löschen
					if event.key == pygame.K_BACKSPACE:
						user_text = user_text[:-1]

					user_text += event.unicode


		screen.fill((0,102,0))

		if active:
			color = color_active

		else:
			color = color_passive

		pygame.draw.rect(screen,color,input_rect,2)

		text_surface = font.render(user_text, True,(255,255,255))
		screen.blit(text_surface,(input_rect.x + 5,input_rect.y - 4))

		input_rect.w = max(150,text_surface.get_width() + 10)
		
		pygame.display.flip()
		clock.tick(60)






#Beginn Spiel
apfelCoords.append(apfelCoordGen())
 
go = True
anhang = None
apfelInd = -1
ende = False
score = 0
coll = False
insert = False

#Erst beginnen wenn Name eingegeben wurde
if entered == True:
	countdown()
	
	while go:
		#Reagiert auf Pfeiltaste
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	        	sys.exit()
	        if event.type == pygame.KEYDOWN:
	            if event.key == pygame.K_UP and richtung != 2:
	                richtung = 0
	                #Richtung 0 heisst nach oben
	            if event.key == pygame.K_RIGHT and richtung != 3:
	                richtung = 1
	                #Richtung 1 heisst nach rechts
	            if event.key == pygame.K_DOWN and richtung != 0:
	                richtung = 2
	                #Richtung 2 heisst nach unten
	            if event.key == pygame.K_LEFT and richtung != 1:
	                richtung = 3
	                #Richtung 3 heisst nach links
	 
	    if anhang != None:
	        schlange.append(anhang.copy())
	        anhang = None
	        apfelCoords.pop(apfelInd)
	 
	    zahl = len(schlange)-1
	    for i in range(1,len(schlange)):
	        schlange[zahl] = schlange[zahl-1].copy()
	        zahl -= 1
	 	
	 	#Ändert Richtung der Schlange
	    if richtung == 0:
	        schlange[0][1] -= 1
	    if richtung == 1:
	        schlange[0][0] += 1
	    if richtung == 2:
	        schlange[0][1] += 1
	    if richtung == 3:
	        schlange[0][0] -= 1
	 
	    for x in range(1,len(schlange)):
	        if schlange[0] == schlange[x]:
	            ende = True

	 	#Prüft auf Kollision
	    if schlange[0][0] < 0 or schlange[0][0] > 27:
	        ende = True

		#Prüft auf Kollision 
	    if schlange[0][1] < 0 or schlange[0][1] > 27:
	        ende = True
	 
	    for x in range(0,len(apfelCoords)):
	        if apfelCoords[x] == schlange[0]:
	            anhang = schlange[-1].copy()
	            apfelInd = x
	            score += 10
	 
	    zufall = np.random.randint(0,100)
	    if zufall <= 1 and len(apfelCoords) < 2 or len(apfelCoords) == 0:
	        apfelCoords.append(apfelCoordGen())
	 
	    if ende == False:
		    zeichner()
		    textGrund,textKasten = textObjekt("Score: " + str(score),font)
		    textKasten.center = ((350,40))
		    screen.blit(textGrund,textKasten)
		    pygame.display.update()
	    elif ende == True:
		    zeichner()
		    textGrund,textKasten = textObjekt("Du hast " + str(score) + " Punkte erreicht",font)
		    textKasten.center = ((350,40))
		    screen.blit(textGrund,textKasten)
		    textGrund,textKasten = textObjekt("GAME OVER",fontBig)
		    textKasten.center = ((350,295))
		    screen.blit(textGrund,textKasten)
		    pygame.display.update()
		    time.sleep(5)
		    partikel = 25
		    schlange = [[13,13],[13,14]]
		    apfelCoords = []
		    richtung = 0
		    go = True
		    anhang = None
		    apfelInd = -1
		    ende = False
		    score = 0
		    coll = False
		    insert = True
	    clock.tick(10)

	


#Datenbankverbindung
#Insertet erst wenn spiel fertig ist

if insert == True:
	
	print("test")
	db = mysql.connector.connect(
		host="localhost",
		user="root",
		password="12345Root",
		database="playerdata1",
		port="3307"
		)
	mycursor = db.cursor()
	go = True
	sql = "INSERT INTO playerdata_real (name, score) VALUES (%s, %s)"
	val = (name, score)
	mycursor.execute(sql, val)

	db.commit()
	insert = False