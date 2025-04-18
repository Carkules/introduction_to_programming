"""
Task 1: Implement your own Rocket class with the following properties:
-> the __init__ method initializes the rocket's position (the default is (0, 0)),
-> the move method moves the rocket by x along the X axis and by y along the Y axis,
-> the get_position method prints the rocket's position on the plane,
-> the get_distance method calculates the distance between the selected rocket and another rocket,
Task 2: Create an object of the Rocket class. Move it on the screen. 
After each move, print its position to the screen.
Task 3: Create a fleet of 5 rockets. Initialize each of them with randomly
chosen coordinates. Move the rockets around the screen. 
After each move, display their positions and the distances between them on the screen.
"""

import math
import random
import matplotlib.pyplot as plt
class Rocket:
    def __init__(self):             #setting starting position in (0, 0)
        self.x = 0
        self.y = 0
        self.r = 1                  #range of the rocket
        r = random.random()         
        g = random.random()
        b = random.random()
        self.c = (r, g, b)          #color of the rocket
    
    def move(self, dx, dy):         #moving the rocket by vector
        self.x += dx
        self.y += dy
    
    def move_rand(self):                            #moving the rocket by random vector
        self.x += random.randint(-100, 100)*0.1
        self.y += random.randint(-100, 100)*0.1
        self.x = round(self.x, 1)
        self.y = round(self.y, 1)
    
    def get_position(self):         #getting the position of the rocket
        return (self.x, self.y)
    
    def get_distance(self, other):  #getting distance between two rockets
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)
    
    
    def draw_rocket(self):                  #function getting needed data to draw a rocket
        drawing_rocket = plt.Circle((self.x, self.y), self.r, color = self.c)
        return drawing_rocket
    
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

def gen_rand_rockets(a):      #funkcja generating 'a' rockets
    rockets = []
    for i in range(a):
        ro = Rocket()
        ro.move_rand()
        rockets.append(ro)
    return rockets

def draw_rockets(rockets):          #funkcja drawing rockets
    figure, axes = plt.subplots()
    axes.set_aspect(1)
    for i in rockets:
        axes.add_artist(i.draw_rocket())
    xl = []
    yl = []
    for i in rockets:
        xl.append(i.x)
        yl.append(i.y)

    plt.xlim(min(xl) - 1, max(xl) + 1)
    plt.ylim(min(yl) - 1, max(yl) + 1)
    plt.show()

def rockets_to_str(rockets):
    str_rockets = []
    for i in rockets:
        str_rockets.append(str(i))
    return str_rockets

rockets = gen_rand_rockets(5)
print(rockets_to_str(rockets))
draw_rockets(rockets)
for i in range(5):          #making five random moves by each rocket
    for j in rockets:
        j.move_rand()
    print(rockets_to_str(rockets))
    draw_rockets(rockets)

def furthest_rocket(rockets):     #funkcja checking which rocket travelled the longest distance
    start = Rocket()
    distances = []
    m = 0
    for i in rockets:
        dist = i.get_distance(start)
        distances.append(dist)
        if m < dist:
            m = dist
            color = i.c
    print("The longest distance was covered by a rocket in color %s. This distance is equal %s." % (color, m))

furthest_rocket(rockets)