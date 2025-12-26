from vec3 import vec3, point3

class ray:
    def __init__(self, origin=point3(0,0,0), direction=point3(0,0,0)):
        self.orig = origin
        self.dire = direction
    def at(self, t):
        return self.orig + self.dire*t

#je = vec3(2,2,2)
#zz = vec3(1,1,1)
#jezz=ray(je,zz)
#bean=jezz.at(7)
#print(bean.so())
