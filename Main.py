import pgzrun
import random

WIDTH=600
HEIGHT=450

ship=Actor("ship.png")
SpaceRock=Actor("spacerocksprite.png")

ship.pos=100,300
SpaceRock.x = 200
SpaceRock.y = 100
msg = "6:00am commence your work"

def draw():

    screen.blit("spacebackground",(0,0))
    ship.draw()
    SpaceRock.draw()
    screen.draw.text(msg, (100,300))    


pgzrun.go()