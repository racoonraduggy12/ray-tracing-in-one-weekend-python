import math
import logging
import numpy as np
from vec3 import vec3, point3

logger = logging.getLogger(__name__)
logging.basicConfig(filename='raytracingweekend.log', level=logging.INFO)


test = vec3(123,223,323)
stuff = point3(1,2,3)
test = test.cross(stuff)
stuff = stuff.unit_vector()
logger.info(str(test.x())+" "+str(test.y())+" "+str(test.z()))
logger.info(str(stuff.x())+" "+str(stuff.y())+" "+str(stuff.z()))
logger.info(str(test.dot(stuff)))
logger.info(stuff.so())
logger.info(test)
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
