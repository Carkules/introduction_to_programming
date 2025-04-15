"""
Many computer games have built-in complex physics engines. One of the functions performed by such engines 
is to detect collisions between objects on the screen. Suppose these objects are approximated by discs on a screen:

Task 1. Come up with a way to represent such discs using one of Python's built-in data types.
Task 2. Write a function that will detect collisions between two discs.
This function should return True if the discs "overlap" each other.
Task 3. Write a function that will move a disc on a screen by a vector given as the second argument.
"""
import math

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

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)
    
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
    
    def __str__(self):
        return "(%s, %s), %s" % (self.s.x, self.s.y, self.r)


p1 = Point(0, 0)
p2 = Point(0.5, 0)
circle1 = circle(p1, 1)
circle2 = circle(p2, 1)
print(circle1.detect_collision(circle2))
print(circle1)
v = Point(1, 2)
circle1.translate_circle(v)
print(circle1)
s = str(p1)




