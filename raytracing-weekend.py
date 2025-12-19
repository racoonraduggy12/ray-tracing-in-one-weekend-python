import math
import logging
import numpy as np

logger = logging.getLogger(__name__)

logging.basicConfig(filename='raytracingweekend.log', level=logging.INFO)

class vec3:
    def __init__(self, e0=0, e1=0, e2=0):
        e = [e0, e1, e2]
        e = np.array(e)
        self.e = e
    def x(self):
        return self.e[0]
    def y(self):
        return self.e[1]
    def z(self):
        return self.e[2]
    def __neg__(self):
        return vec3(-self.e[0], -self.e[1], -self.e[2])
    def __getitem__(self, key):
        return self.e[key]
    def __setitem__(self, key, value):
        self.e[key] = value
    def __iadd__(self, other):
        self.e[0] += other.e[0]
        self.e[1] += other.e[1]
        self.e[2] += other.e[2]
        return vec3(self.e[0], self.e[1], self.e[2])
    def __
test = vec3(1,2,3)
stuff = vec3(1,2,3)
test += stuff
test[0] = 12
logger.info(str(test.x())+str(test.y())+str(test.z()))
#logger.info(test)
image_height = 256
image_width = 256
print("P3\n"+str(image_width)+' '+str(image_height)+"\n255\n")

j = 0
while j < image_height:
    i = 0
    logger.info("\rScanlines remaining: "+str(image_height-j))
    while i < image_width:
        r = i/(image_width-1)
        g = j/(image_height-1)
        b = 0.00

        ir = round(254.99 * r)
        ig = round(254.99 * g)
        ib = round(254.99 * b)

        print(str(ir)+' '+str(ig)+' '+str(ib)+'\n')
        i += 1
    j += 1
