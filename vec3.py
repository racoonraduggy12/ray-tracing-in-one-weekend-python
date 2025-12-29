import numpy as np
import math

#3 diminsional vector class
class vec3:

#initialize
    def __init__(self, e0=0, e1=0, e2=0):
        e = [e0, e1, e2]
        e = np.array(e)
        self.e = e

#x, y and z getters
    def x(self):
        return self.e[0]
    def y(self):
        return self.e[1]
    def z(self):
        return self.e[2]

#negation (unaray -) function override
    def __neg__(self):
        return vec3(-self.e[0], -self.e[1], -self.e[2])

#indexing overrides
    def __getitem__(self, key):
        return self.e[key]
    def __setitem__(self, key, value):
        self.e[key] = value

    def __iadd__(self, other):
        self.e[0] += other.e[0]
        self.e[1] += other.e[1]
        self.e[2] += other.e[2]
        return self

    def __imul__(self, other):
        self.e[0] *= other
        self.e[1] *= other
        self.e[2] *= other
        return self

    def __itruediv__(self, other):
        self.e[0] /= other
        self.e[1] /= other
        self.e[2] /= other
        return self
#vector magnatude getter
    def length_squared(self):
        return self.e[0]*self.e[0] + self.e[1]*self.e[1] + self.e[2]*self.e[2]
    def length(self):
        return math.sqrt(self.length_squared())

#addition, multiplication and division ovverrides
    def __add__(self, other):
        try:
            return vec3(self.e[0]+other.e[0], self.e[1]+other.e[1], self.e[2]+other.e[2])
        except:
            return vec3(self.e[0]+other, self.e[1]+other, self.e[2]+other)
    def __mul__(self, other):
        try:
            return vec3(self.e[0]*other.e[0], self.e[1]*other.e[1], self.e[2]*other.e[2])
        except:
            return vec3(self.e[0]*other, self.e[1]*other, self.e[2]*other)
    def __truediv__(self, other):
        return self * (1/other)
    def __sub__(self, other):
        return vec3(self.e[0]-other.e[0], self.e[1]-other.e[1], self.e[2]-other.e[2])

#dot-production function
    def dot(self, other):
        return self.e[0] * other.e[0] + self.e[1] * other.e[1] + self.e[2] * other.e[2]

#cross product function
    def cross(self, other):
        return vec3(self.e[1] * other.e[2] - self.e[2] * other.e[1], self.e[2] * other.e[0] - self.e[0] * other.e[2], self.e[0] * other.e[1] - self.e[1] * other.e[0])

#unit vector function
    def unit_vector(self):
        return self / self.length()

#string output function
    def so(self):
        return str(self.e[0])+' '+str(self.e[1])+' '+str(self.e[2])

#alias point3 as vec3
point3 = vec3
