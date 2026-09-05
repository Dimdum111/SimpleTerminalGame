import time
import keyboard
import random

plrstates = ["▲", "▼", "◄", "►"]
score = 0

# Colours!! Using ascii codes to colour it!
red = "\033[31m"
yellow = "\033[33m"
blue_back = "\033[44m"
reset = "\033[0m"

coin = f"{yellow}${reset}"
plr = plrstates[3]

# Game map, You can build anything, and w/h will automaticly adjust.
map = [
    "█████████████████████████████████",
    "█                   █           █",
    "█    ████                   █   █",
    "█         ██         █      █   █",
    "█         █                 █   █",
    "█         █         ██          █",
    "█                   █           █",
    "█████████████████████████████████",
]

wight = len(map[0])
height= len(map)
x,y = 1,1

# Clearing the terminal and disabling the cursor
print("\033[H\033[2J\033[3J", end="")
print("\033[?25l")

# spawn_coin , it randomly places a coin and retries if there is a wall, then when all conditions are satisfied: returns it's x and y so main game loop can place it
def spawn_coin():
    while True:
        coinplacex = random.randint(1, wight - 2)
        coinplacey = random.randint(1, height - 2)
        if map[coinplacey][coinplacex] != "█":
            return coinplacex, coinplacey

# Gets the coordinates the first time because if we would place it in the game loop it would repeatedly change it's x/y and jump across the map.
# so we spawn it before and then when picking up we set new coordinates
coinx, coiny = spawn_coin()

# MAIN GAME LOOP
while True:
    xnew, ynew, = x,y
    
    # input handler
    if keyboard.is_pressed("w"):
        ynew -= 1
        plr = plrstates[0]
    elif keyboard.is_pressed("s"):
        ynew += 1
        plr = plrstates[1]
    elif keyboard.is_pressed("a"):
        xnew -= 1
        plr = plrstates[2]
    elif keyboard.is_pressed("d"):
        xnew += 1
        plr = plrstates[3]
    elif keyboard.is_pressed("q"):
        print("\033[H\033[2J\033[3J", end="") # clears the screen
        exit()
    
    # Checking collision, if not collides: change x/y to new coordinates. else: don't.
    if map[ynew][xnew] != "█":
        x,y = xnew, ynew
    
    # Checking coin collision, if collides: adds 1 to score and spawns new coin
    if x == coinx and y == coiny:
        score += 1
        coinx, coiny = spawn_coin()
    
    # Prepares to draw everything, also places the coin and player
    grid = [list(row) for row in map]
    grid[y][x] = f"{red}{plr}{reset}"
    grid[coiny][coinx] = coin
    
    # Draws the screen and sleeps.
    output = "\033[H" + "\n".join("".join(row) for row in grid)
    print(f"{output}\nScore: {blue_back}{score}{reset}", end="")
    time.sleep(0.07)