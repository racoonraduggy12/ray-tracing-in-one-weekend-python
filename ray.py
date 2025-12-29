from vec3 import vec3, point3

class ray:
    def __init__(self, orig=point3(0,0,0), dire=vec3(0,0,0)):
        self.orig = orig
        self.dire = dire
    def at(self, t):
        return self.orig + self.dire*t
    def origin(self):
        return self.orig
    def direction(self):
        return self.dire
#__________________________TESTING___________________________
#je = vec3(2,2,2)
#zz = vec3(1,1,1)
#jezz=ray(je,zz)
#bean=jezz.at(7)
#jezz.origin()
#jezz.direction()
#print(bean.so())
#____________________________________________________________
