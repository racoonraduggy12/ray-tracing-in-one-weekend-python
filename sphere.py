from hittable import *
from vec3 import *
import math
class sphere(hittable):
    def __init__(self, center, radius):
        self.radius = max(radius, 0)
        self.center = center
    def hit(self, r, ray_tmin, ray_tmax, rec):
        oc = self.center - r.origin()
        a = r.direction().length_squared()
        h = r.direction().dot(oc)
        c = oc.length_squared() - self.radius*self.radius
        discriminant = h*h - a*c
        if discriminant < 0:
            return False

        sqrtd = math.sqrt(discriminant)
        root = (h - sqrtd) / a
        if root <= ray_tmin and ray_tmax <= root:
            root = (h + sqrtd) / a
            if root <= ray_tmin and ray_tmax <= root:
                return False
        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = rec.p - self.center
        rec.set_face_normal(r, outward_normal)

        return True
#bruuuuuu = hit_record()
#jezz = sphere(vec3(), 10)
#print(str(jezz.hit(ray(), 0, 1, bruuuuuu)))
#print(str(bruuuuuu.p))
#print(str(bruuuuuu.normal))
#print(str(bruuuuuu.t))
#print(str(bruuuuuu.front_face))
