import add_curve_points


def cyclic_curve_points(x, y, p):
    next_x, next_y = x, y
    points = [(next_x, next_y)]
    #overflow of this loop will cause the repetion of points
    for i in range(1,p+5):
        next_x, next_y = add_curve_points.add_points(next_x, next_y, x, y, p)
        points.append((next_x, next_y))

    return points

# note when the overflow occurs we get a point None, None, that is also knows as point at infinity
# although the term here sounds absurd the point is actually on the curve just that it is not a point on the plane
# this point here in group theortical terms is called the identity element
# this element satisfies all the properties of an identity element in a group
# such as adding the identity element to the generator point(can be any point) will give the generator point itself
# also one more interesting thing here is that what is casuing the identity element is adding (4,1) to generator point (4,10)
# which is actualla its inverse
# this is because for every point (x,y) on the curve there is a point (x,y`) on the curve and -y`mod p = 0
# also do note that there will not exist an inverse for a point if the inverse of the point is itself i.e y=0
# the order of the group is the number of points on the curve including the identity element i.e p+1 and not modulous

# consider the generator point to be (4, 10) here and the prime to be 11
print(cyclic_curve_points(4, 10, 11))
