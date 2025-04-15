import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_location(self, x, y):
        self.x = x
        self.y = y
    
    def get_location(self):
        return (self.x, self.y)
    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
        self.x = round(self.x, 1)
        self.y = round(self.y, 1)

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)
    
    def distance_x(self, other):
        dx = abs(self.x - other.x)
        return dx
    
    def distance_y(self, other):
        dy = abs(self.y - other.y)
        return dy
    
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)



class circle:
    def __init__(self, s, r):
        self.s = s
        self.r = r
    
    def detect_collision(self, other):
        dst = self.s.distance(other.s)
        return dst <= self.r + other.r
    
    def translate_circle(self, v):
        self.s.translate(v.x, v.y)
    
    def distance_sx(self, other):
        return self.s.distance_x(other.s)
    
    def distance_sy(self, other):
        return self.s.distance_y(other.s)
    
    def draw_circle(self):
        drawing_circle = plt.Circle((self.s.x, self.s.y), self.r, fill = False)
        return drawing_circle
    
    def __str__(self):
        return "(%s, %s), %s" % (self.s.x, self.s.y, self.r)
    

