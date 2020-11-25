import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def rotation(self):
        return math.atan2(self.y, self.x)
    @property
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
    def __mul__(self, other):
        if type(other) == Vector2:
            return Vector2(self.x * other.x, self.y * other.y)
        return Vector2(self.x * other, self.y * other)
    def __imul__(self, other):
        if type(other) == Vector2:
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other
    def __div__(self, other):
        if type(other) == Vector2:
            return Vector2(self.x / other.x, self.y / other.y)
        return Vector2(self.x / other, self.y / other)
    def __idiv__(self, other):
        if type(other) == Vector2:
            self.x / other.x
            self.y / other.y
        else:
            self.x /other
            self.y / other
    def rotate(self, theta):
        return Vector2((self.x * math.cos(theta)) - (self.y * math.sin(theta)), (self.x * math.sin(theta)) + (self.y * math.cos(theta)))
    def dist(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
    def normalize(self):
        div = math.sqrt(self.x**2 + self.y**2)
        self.x = self.x / div
        self.y = self.y / div
    def __str__(self):
        return '<x: ' + str(self.x) + ', ' + ' y: ' + str(self.y) + '>'
    
