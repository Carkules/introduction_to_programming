"""
Write a program that on a plane -15 <= x, y <= 15 
arranges randomly 100 discs of radius r = 0.5,
detects collisions,
moves the discs so they don't overlap.
"""


import disc as d
import random as r
import matplotlib.pyplot as plt
import copy

rang = 0.5

def gen_rand_discs(a):
    discs = []
    for i in range(a):
        discs.append(d.circle(d.Point(round(r.uniform(-14.5, 14.5), 1), round(r.uniform(-14.5, 14.5), 1)), 0.5))
    return discs

discs = gen_rand_discs(100)
original_discs = copy.deepcopy(discs)

def discs_to_str(discs):
    discs_str = []  
    for i in discs:
        s = str(i)
        discs_str.append(s)
    return discs_str

def draw_discs(original_discs, discs):
    figure, axes = plt.subplots(1, 2, figsize=(10, 5))
    plt.subplot(1,2,2)
    ax = axes[1]
    ax.set_aspect(1)
    for i in discs:
        ax.add_artist(i.draw_circle())

    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)

    plt.subplot(1,2,1)
    ax = axes[0]
    ax.set_aspect(1)
    for i in original_discs:
        ax.add_artist(i.draw_circle())

    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    plt.show()


l = len(discs)

flag = 0
while flag == 0:
    tempflag = 0
    for i in range(0, l):
        for j in range(i + 1, l):
            while discs[i].detect_collision(discs[j]):   
                tempflag = 1
                if discs[i] == discs[j]:
                    discs[i].translate_circle(d.Point(rang, 0))
                    discs[j].translate_circle(d.Point(0, rang))

                dx = round(discs[i].distance_sx(discs[j]), 1)
                dy = round(discs[i].distance_sy(discs[j]), 1)
                #print(dx, dy)

                discs[i].translate_circle(d.Point(dx, dy))
                discs[j].translate_circle(d.Point(-dx, -dy))

                if abs(discs[i].s.x) > 14.5:
                    if discs[i].s.x > 14.5:
                        discs[i].translate_circle(d.Point(14.5-discs[i].s.x, 0))
                    else:
                        discs[i].translate_circle(d.Point(discs[i].s.x - 14.5, 0))
                if abs(discs[i].s.y) > 14.5:
                    if discs[i].s.y > 14.5:
                        discs[i].translate_circle(d.Point(0, 14.5-discs[i].s.y))
                    else:
                        discs[i].translate_circle(d.Point(0, discs[i].s.y - 14.5))
                if abs(discs[j].s.x) > 14.5:
                    if discs[j].s.x > 14.5:
                        discs[j].translate_circle(d.Point(14.5-discs[j].s.x, 0))
                    else:
                        discs[j].translate_circle(d.Point(discs[j].s.x - 14.5, 0))
                if abs(discs[j].s.y) > 14.5:
                    if discs[j].s.y > 14.5:
                        discs[j].translate_circle(d.Point(0, 14.5-discs[j].s.y))
                    else:
                        discs[j].translate_circle(d.Point(0, discs[j].s.y - 14.5))


    if tempflag == 0:
        flag = 1


print("")

print(discs_to_str(discs))
print(discs_to_str(original_discs))
draw_discs(original_discs, discs)
