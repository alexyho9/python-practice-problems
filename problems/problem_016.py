# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.

def is_inside_bounds(x, y):
    if x > 10 or x < 0:
        return False
    if y > 10 or y < 0:
        return False
    return True


x1 = 4
y1 = 10

x2 = 9
y2 = 12

x3 = 9
y3 = -6

print(is_inside_bounds(x1, y1))
print(is_inside_bounds(x2, y2))
print(is_inside_bounds(x3, y3))
