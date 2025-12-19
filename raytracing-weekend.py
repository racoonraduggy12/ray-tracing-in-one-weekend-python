import math
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(filename='raytracingweekend.log', level=logging.INFO)

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
        b = 0.0

        ir = round(254.99 * r)
        ig = round(254.99 * g)
        ib = round(254.99 * b)

        print(str(ir)+' '+str(ig)+' '+str(ib)+'\n')
        i += 1
    j += 1
