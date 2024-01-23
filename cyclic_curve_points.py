import add_curve_points

# refer elliptic_curve_plot.py for the plot of the curve


def cyclic_curve_points(x, y, p):
    next_x, next_y = x, y
    points = [(next_x, next_y)]
    # overflow of this loop will cause the repetion of points
    for i in range(1, p+1):
        next_x, next_y = add_curve_points.add_points(next_x, next_y, x, y, p)
        points.append((next_x, next_y))

    return points

# the 12th(p+1th/ curve_order) point is: (None, None) the point at infinity!
# this point here in group theortical terms is called the identity element
# this element satisfies all the properties of an identity element in a group
# such as adding the identity element to the generator point(can be any point) will give the generator point itself
# since the generator point is (4, 10) and adding that point to pth (11th) point: P1*x = inv(P1*(curve_order-x)) = (4, 1)
# proves that (None, None) is the identity element and in this context it is called the point at infinity
# and adding any element to the identity element will give the element itself ===> the points start repeating there by
# for every point (x,y) on the curve there is a point (x,y`) on the curve such that ymodp +y`modp=0: where (x,y`) is the inverse of (x,y)
# there will not exist an inverse for a point if the inverse of the point is itself ====> y=0


# consider the generator point to be (4, 10) here and the prime to be 11
print(cyclic_curve_points(4, 10, 11))
