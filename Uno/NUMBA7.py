import pgzrun
import pygame
import time

WIDTH = 900
HEIGHT = 700
tim = pygame.mixer.Sound("Uno\_tensectimer.wav")
timout = pygame.mixer.Sound("Uno\_time!.wav")
end = pygame.mixer.Sound("Uno\_victory2.wav")

lvl = 0

tim.play()

tims = time.time()
totl = -2

opts = []
go = Actor("onward!")
go.pos = 830, 70

for i in range(4):
    opt = Actor("button1")
    opts.append(opt)

opts[0].pos = 120, 240
opts[1].pos = 560, 240
opts[2].pos = 120, 630
opts[3].pos = 560, 630

quests = []

with open("Uno\quqq.txt","r") as file:
    data = file.readlines()
    for line in data:
        quest_data = line.split(",")
        quest_dict = {
            "question": quest_data[0],
            "options": quest_data[1:5],
            "answer": int(quest_data[5])
        }
        quests.append(quest_dict)

def draw():
    screen.blit("void2",(0,0))
    for i in range(4):
        opts[i].draw()
    go.draw()
    totl = time.time() - (10 + tims)
    screen.draw.text(f"{(round(totl,0)) + ((round(totl,0)) * 2)}",center = (100,50))
    screen.draw.text(quests[lvl][0],center = (300,50))

    for i in range(4):
        screen.draw.text(quests[lvl][i+1],center = (opts[i].pos))

def update():
    global tims, totl
    if totl == 0:
        timout.play()
        time.sleep(3)
        lvl += 1
        tim.play()

        tims = time.time()
        totl = -2
    
    pass

pgzrun.go()