def checkio(data):
    data = data.replace("(", "").replace(")", "").split(",")
    x1, y1, x2, y2, x3, y3 = [int(i) for i in data]
    a = x2 - x1
    b = y2 - y1
    c = x3 - x1
    d = y3 - y1
    e = a * (x1 + x2) + b * (y1 + y2)
    f = c * (x1 + x3) + d * (y1 + y3)
    g = 2 * (a * (y3 - y2) - b * (x3 - x2))
    cx = (d * e - b * f) / g
    cy = (a * f - c * e) / g
    r = ((x1 - cx)**2 + (y1 - cy)**2)**0.5
    return "(x-{:g})^2+(y-{:g})^2={:g}^2".format(round(cx, 2), round(cy, 2), round(r, 2))

if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"

