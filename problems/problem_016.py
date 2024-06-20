# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.

def is_inside_bounds(x, y):
    for num in x:
        if num > 10 or num < 0:
            return False
    for num in y:
        if num > 10 or num < 0:
            return False
    return True


x1 = (4, 7)
y1 = (10, 2)

x2 = (9, 3)
y2 = (12, 1)

x3 = (9, 3)
y3 = (-6, 1)

print(is_inside_bounds(x1, y1))
print(is_inside_bounds(x2, y2))
print(is_inside_bounds(x3, y3))
