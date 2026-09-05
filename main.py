import time
import keyboard
import random

plrstates = ["▲", "▼", "◄", "►"]
coin = "$"
score = 0

plr = plrstates[3]
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

print("\033[?25l")

def spawn_coin():
    while True:
        coinplacex = random.randint(1, wight - 2)
        coinplacey = random.randint(1, height - 2)
        if map[coinplacey][coinplacex] != "█":
            return coinplacex, coinplacey

coinx, coiny = spawn_coin()

while True:
    xnew, ynew, = x,y
    
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
        exit()
    
    if map[ynew][xnew] != "█":
        x,y = xnew, ynew
    
    if x == coinx and y == coiny:
        score += 1
        coinx, coiny = spawn_coin()
    
    grid = [list(row) for row in map]
    grid[y][x] = plr
    grid[coiny][coinx] = coin
    
    output = "\033[H" + "\n".join("".join(row) for row in grid)
    print(f"{output}\nScore: {score}", end="")
    time.sleep(0.07)