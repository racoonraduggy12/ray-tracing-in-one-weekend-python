from vec3 import vec3, point3

color = vec3

def write_color(pixel_color):
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    rbyte = round(255.99 * r)
    gbyte = round(255.99 * g)
    bbyte = round(255.99 * b)

    return str(rbyte) + ' ' + str(gbyte) + ' ' + str(bbyte) + '\n'
