import pgzrun
import pygame
import time

WIDTH = 900
HEIGHT = 700
tim = pygame.mixer.Sound("Uno\_tensectimer.wav")
timout = pygame.mixer.Sound("Uno\_time!.wav")
end = pygame.mixer.Sound("Uno\_victory2.wav")
wrong = pygame.mixer.Sound("Uno\wrong.wav")

lvl = 0
score = 0

j = False

tim.play()

tims = 10
totl = -1

opts = []
go = Actor("onward!")
go.pos = 830, 70

for i in range(4):
    opt = Actor("button1")
    opts.append(opt)
g = []
g.append(go)

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

rectan = Rect((75,110),(500,75))

def draw():
    screen.blit("void2",(0,0))
    if j == False:
        for i in range(4):
            opts[i].draw()
        for i in range(1):
            g[i].draw()
        totl = time.time() - (10 + tims)
        screen.draw.text(str(tims),center = (800,350), fontsize = 150)
        # screen.draw.text(quests[lvl]["question"],center = (300,50))
        screen.draw.filled_rect(rectan,"grey")
        screen.draw.textbox(quests[lvl]["question"],rectan,color="white")

        for i in range(4):
            screen.draw.text(quests[lvl]["options"][i],center = (opts[i].pos))
    if j == True:
        screen.draw.text(f"Score:{score}/11",center = (450,350),fontsize = (125),color = ("white"))

def update():
    pass

def update_time():
    global tims, lvl
    if j == True:
        return
    if tims > 0:
        tims -= 1
    else:
        timout.play()
        time.sleep(4)
        lvl += 1
        tims = 10
        tim.play()

def on_mouse_down(pos):
    global tims, lvl, score, j
    cord = pos
    if go.collidepoint(pos):
        if j == False:
            tim.stop()
            tims = 10
            lvl += 1
            if lvl > 10:
                j = True
            tim.play()
    for i in range(4):
        if opts[i].collidepoint(pos):
            if i+1 == quests[lvl]["answer"]:
                tim.stop()
                if j == False:
                    lvl += 1
                    score += 1
                    tims = 10
                    tim.play()
            else:
                tim.stop()
                wrong.play()
                time.sleep(1)
                if j == False:
                    lvl += 1
                    tims = 10
                    tim.play()
    if lvl > 10:
        j = True
        tim.stop()
        end.play()


clock.schedule_interval(update_time,0.95)

pgzrun.go()