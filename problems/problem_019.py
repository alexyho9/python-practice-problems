# Complete the is_inside_bounds function which has the
# following parameters:
#   x: the x coordinate to check
#   y: the y coordinate to check
#   rect_x: The left of the rectangle
#   rect_y: The bottom of the rectangle
#   rect_width: The width of the rectangle
#   rect_height: The height of the rectangle
#
# The is_inside_bounds function returns true if all of
# the following are true
#   * x is greater than or equal to rect_x
#   * y is greater than or equal to rect_y
#   * x is less than or equal to rect_x + rect_width
#   * y is less than or equal to rect_y + rect_height

set1 = [5, 5, 0, 0, 10, 10]
set2 = [5, 5, 6, 6, 10, 10]

def is_inside_bounds(x, y, rect_x, rect_y, rect_width, rect_height):
    # test x coordinates
    x_ok = rect_x <= x <= rect_x + rect_width
    # test y coordinates
    y_ok = rect_y <= y <= rect_y + rect_height
    # evaluate x and y ok
    return x_ok and y_ok

print(is_inside_bounds(5, 5, 0, 0, 10, 10))
print(is_inside_bounds(5, 5, 6, 6, 10, 10))
