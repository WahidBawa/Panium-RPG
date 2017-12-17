#CHARtest.py
from pygame import *
size = (800,600)
screen = display.set_mode(size)
screen.fill((255,255,255))
CHARexp =    [ 2,        1,        1]
CHAR =       ['Lindus', 'Nimbus', 'Dingus']
CHARlevels = [ 1,        1,        1]
CharStats = ['Attack', 'Speed', 'Dexterity']
LindusStats = [5,       8,       9]
NimbusStats = [5,       10,      12]
DingusStats = [2,       7,       6]
curChar = "Lindus"
running = True
from pygame import * 
size=(800,600)
screen = display.set_mode(size)
screen.fill((255,255,255)) 
enemy = ""                     
running = True
def hardEnemy():
	if curChar == "Lindus":
		charInd = CHAR.index("Lindus")
		obtainedEXP = CHARexp[charInd]/(40/CHARlevels[charInd])
		EXPupdate = obtainedEXP + CHARexp[charInd]
		CHARexp[0] = EXPupdate
		print(CHARexp[0])
		# CHARexp[0] + EXPupdate
while running:
	for evt in event.get(): 
		if evt.type == QUIT:
			running = False
		if evt.type == MOUSEBUTTONDOWN:
			if evt.button == 3:
				print("Lindus: ",CharStats)
				print("EXP: ",CHARexp)

			if evt.button == 1:
				if enemy == "Hard":
					# time.delay(100)
					print("Hard")
					hardEnemy()
		
		if evt.type == KEYDOWN:
			if evt.key == K_ESCAPE:
				running=False       
	####

	hardRect=Rect(0,0,80,80)
	mediumRect=Rect(100,0,80,80)
	easyRect=Rect(200,0,80,80)
	####
	mx,my=mouse.get_pos()
	mb=mouse.get_pressed()
	####
	if mb[0]:
		if hardRect.collidepoint(mx,my):
			enemy="Hard"
		if mediumRect.collidepoint(mx,my):
			enemy="Medium"
		if easyRect.collidepoint(mx,my):
			enemy="Easy"		
	####
	draw.rect(screen, (255,0,0), hardRect)
	draw.rect(screen, (255,255,0), mediumRect)
	draw.rect(screen, (0,255,0), easyRect)

	# if mb[0]:
	# 	if enemy == "Hard":
	# 		time.delay(100)
	# 		print("Hard")
	# 		hardEnemy()
	# 	if enemy == "Medium":
	# 		time.delay(100)
	# 		print("Medium")
	# 	if enemy == "Easy":
	# 		time.delay(100)
	# 		print("Easy")		

	display.flip() 
quit() 