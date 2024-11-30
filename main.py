import pgzrun  # Add this import to run the Pygame Zero game
import random  # Keep the random import

WIDTH = 1000 
HEIGHT = 500 

TITLE = "MOCO GAME" 
FPS = 30 

# Game States
mode = 'welcome'  # Changed initial mode to 'welcome'

# Actors
welcome = Actor("welcome", (WIDTH/2, HEIGHT/2))  # Welcome screen image
play_button = Actor("play", (WIDTH/3, HEIGHT/3 + 100))
store = Actor("store", (WIDTH/1.5, HEIGHT/1.5 -60))  # Store button
circle = Actor('circle', (50, 470))
background = Actor("bacground")
build = Actor('build', (450, 490))
thorn = Actor('thorn', (750, 490))
thorn_fijo = Actor('thorn', (500, 490))
go = Actor('go', (WIDTH/2, HEIGHT/2))  # Game Over screen

# Game Variables
game_over = 0
new_image = 'circle'

def draw():
    # Welcome Screen
    if mode == 'welcome':
        welcome.draw()
        play_button.draw()
        store.draw()
    
    # Game Screen
    elif mode == 'game':
        background.draw()
        circle.draw()
        build.draw()
        thorn.draw()
        thorn_fijo.draw()
        
        # Draw game over screen when game is over
        if game_over == 1:
            go.draw()
            circle.image = 'hurt'

def update(dt):
    global new_image
    global game_over
    
    # Only update game elements if in game mode and not game over
    if mode == 'game' and game_over == 0:
        # Thorn movement
        if thorn.x > -20:
            thorn.x = thorn.x - 5
        else:
            thorn.x = WIDTH + 20
        
        # Build movement
        if build.x > -20:
            build.x = build.x - 5
        else:
            build.x = WIDTH + 20

        # Player controls
        if keyboard.left or keyboard.a and circle.x > 20:
            circle.x = circle.x - 5
            if new_image != 'left':
                circle.image = 'left'
                new_image = 'left'
        elif keyboard.right or keyboard.d and circle.x < 580:
            circle.x = circle.x + 5
            if new_image != 'right':
                circle.image = 'right'
                new_image = 'right'
        
        # Collision detection
        if circle.colliderect(build) or circle.colliderect(thorn) or circle.colliderect(thorn_fijo):
            game_over = 1

def on_mouse_down(pos, button):
    global mode
    
    # Start game when play button is clicked on welcome screen
    if mode == 'welcome':
        if play_button.collidepoint(pos):
            mode = 'game'
        elif store.collidepoint(pos):
            mode = 'store'  # Add a new store mode

def on_key_down(key):
    global game_over
    global mode
    
    # Jump mechanism only in game mode
    if mode == 'game':
        # Jump
        if (keyboard.space or keyboard.up or keyboard.w) and game_over == 0:
            circle.y = 350
            animate(circle, tween='bounce_end', duration=2, y=470)
        
        # Reset game when Enter is pressed in game over state
        if game_over == 1 and keyboard.enter:
            game_over = 0
            circle.pos = (50, 470)
            circle.image = 'circle'
            build.pos = (450, 490)
            thorn.pos = (750, 490)
            thorn_fijo.pos = (500, 490)

# Add this line to run the game
pgzrun.go()
