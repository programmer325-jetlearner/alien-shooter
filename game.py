import pgzrun
import random

WIDTH=1200
HEIGHT=600
TITLE="galaga game"

#creating variables
score=0
lives=3
is_game_over=False
speed=5
aliens=[]
bullets=[]

#creating the ship
ship=Actor("galaga")
ship.pos=(600,540)


#creating the enemies
for i in range(8):
    alien=Actor("enemy")
    alien.x=random.randint(0,WIDTH-80)
    alien.y=random.randint(-100,0)
    aliens.append(alien)

#create bullets
def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor("bullet")
        bullet.x=ship.x
        bullet.y=ship.y-50
        bullets.append(bullet)

#function to display score/lives
def display_score():
    screen.draw.text(f"score: {score}",(50,30))
    screen.draw.text(f"lives: {lives}",(50,60))


#function for drawing game state
def draw():
    if lives>0:
        screen.clear()
        screen.fill("light blue")
        ship.draw()
        for alien in aliens:
            alien.draw()
        for bullet in bullets:
            bullet.draw()
        display_score()
    else:
        game_over_screen()

        

    



pgzrun.go()