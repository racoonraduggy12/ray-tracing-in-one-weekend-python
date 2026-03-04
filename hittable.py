from ray import *

class hit_record:
    def __init__(self):
        self.p = point3()
        self.normal = vec3()
        self.t: float
        self.front_face: bool
    def set_face_normal(self, r, outward_normal):
        self.front_face = r.direction().dot(outward_normal) < 0
        if self.front_face:
            self.normal = outward_normal
        else:
            self.normal = -outward_normal


class hittable:
    def hit(self, r, ray_tmin, ray_tmax, rec):
        raise NotImplementedError

#truuu = hit_record()
#bruh = hittable()
#bruh.hit(1, 1, 1, truuu)
