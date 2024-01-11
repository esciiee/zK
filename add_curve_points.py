def double_point(x, y, a, p):
    lamd = ((3*x**2) % p*pow(2*y, -1, p)) % p
    x3 = (lamd**2 - 2*x) % p
    y3 = (lamd*(x-x3) - y) % p
    return x3, y3


def add_points(x1, y1, x2, y2, p, a=0):
    if (x1 == y1 == None):
        return x2, y2
    if (x2 == y2 == None):
        return x1, y1

    assert (x2**3 + 3) % p == (y2**2) % p, "Point 2 is not on the curve"
    assert (x1**3 + 3) % p == (y1**2) % p, "Point 1 is not on the curve"

    if (x1 == x2 and y1+y2 == p):
        return None, None

    if (x1 == x2 and y1 == y2):
        return double_point(x1, y1, a, p)

    lamda = (y2 - y1) * pow(x2 - x1, -1, p) % p

    x3 = (lamda**2 - x1 - x2) % p
    y3 = (lamda*(x1 - x3) - y1) % p
    return x3, y3

#print(add_points(4, 10, 4, 1, 11))

export = {
    "add_points": add_points,
    "double_point": double_point
}
