import math
import logging
import numpy as np
from vec3 import vec3, point3
from color import *
from ray import *

#setup python logging
global logger
logger = logging.getLogger(__name__)

logging.basicConfig(filename='raytracingweekend.log', level=logging.INFO)
def hit_sphere(center, radius, r):
    oc = center - r.origin()
    a = r.direction().dot(r.direction())
    b = -2.0 * r.direction().dot(oc)
    c = oc.dot(oc) - radius*radius
    discriminant = b*b - 4*a*c
    return (discriminant >= 0)

def ray_color(r):
    if hit_sphere(point3(0,0,-1), 0.5, r):
        return color(0, 1,0)
    r_direction = r.direction()
    unit_direction = r_direction.unit_vector()
    a = (unit_direction.y() + 1.0)*0.5
    return (color(1.0, 1.0, 1.0)*(1.0-a)) + (color(0.5, 0.7, 1.0)*a)

#image aspectratio height and width
aspect_ratio = 16.0/9.0
image_width = 400
image_height = round(image_width / aspect_ratio)

if image_height < 1:
    image_height = 1
#camera
focal_length = 1.0
viewport_height = 2.0
viewport_width = viewport_height * (image_width/image_height)
camera_center = point3(0, 0, 0)

#calculate the vectors across the hroizontal and down the vertical viewport edges
viewport_u = vec3(viewport_width, 0, 0)
viewport_v = vec3(0, -viewport_height, 0)

#calculate the horizontal and vertical delta vectors from pixel to pixel
pixel_delta_u = viewport_u / image_width
pixel_delta_v = viewport_v / image_height
viewport_upper_left = camera_center - vec3(0, 0, focal_length) - viewport_u/2 - viewport_v/2
pixel00_loc = viewport_upper_left + (pixel_delta_u + pixel_delta_v) * 0.5

#render
print("P3\n"+str(image_width)+' '+str(image_height)+"\n255\n")

j = 0
while j < image_height:
    i = 0
    logger.info("\rScanlines remaining: "+str(image_height-j))
    while i < image_width:
        pixel_center = pixel00_loc + (pixel_delta_u * i) + (pixel_delta_v * j)
        ray_direction = pixel_center - camera_center
        rr = ray(camera_center, ray_direction)

        pixel_color = ray_color(rr)
        print(write_color(pixel_color))
        i += 1
    j += 1
