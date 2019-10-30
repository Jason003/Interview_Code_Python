from math import sin, cos, acos, pi, floor
x1 = 41.836944
y1 = -87.684722
x2 = 40.7127
y2 = -74.0059

def convert(d):
    return d * pi / 180

log_diff = abs(convert(y1 - y2))

angle = acos(sin(convert(x1)) * sin(convert(x2)) + cos(convert(x1)) * cos(convert(x2)) * cos(log_diff))

d = 3963 * angle

print(floor(d))
