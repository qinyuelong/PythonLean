from math import hypot
import ccxt

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)


    def __abs__(self):
        return hypot(self.x , self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)




import os


project_dir = os.path.dirname(os.path.dirname(__file__))
print(project_dir)

print(os.path.dirname(__file__))