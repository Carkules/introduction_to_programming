"""Package the disc function into module."""
import disc 
a = disc.circle(disc.Point(1, 3), 1)
print(a)
a.translate_circle(disc.Point(1, 2))
print(a)