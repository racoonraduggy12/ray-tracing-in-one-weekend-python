import math
import logging
import numpy as np
from vec3 import vec3, point3
from color import *

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
        pixel_color = color(i/(image_width), j/(image_height-1), 0)
        print(write_color(pixel_color))
        i += 1
    j += 1
