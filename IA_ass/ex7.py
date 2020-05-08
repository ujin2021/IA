class Point:
    """2D Point class"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other): #Add magic method
        return (self.x, self.y) == (other.x, other.y)

    def __nq__(self, other): #Add magic method
        return (self.x, self.y) != (other.x, other.y)

    def reflect_x(self):
        # reflection of the point about x-axis
        return repr(Point(self.x, -self.y))

    def slope_from_origin(self):
        # return the slope of the line joining the origin to the point
        try :
            if(self.x == 0 and self.y == 0):
                return "This point is same as origin"
            return (self.y / self.x)
        except ZeroDivisionError:
            return "Slope is infinite"

    def get_line_to(self, other):
        #y = ax + b, print two coefficients as a tuple of two values (a, b)
        try:
            slope = (self.y - other.y) / (self.x - other.x)
            yIntercept = self.y - slope*self.x
            return(slope, yIntercept)
        except ZeroDivisionError:
            return "Slope is infinite"

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def midpoint(self, other):
        """ Return the midpoint of points p1 and p2 """
        mx = (self.x + other.x) / 2
        my = (self.y + other.y) / 2
        return Point(mx, my)


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at Point posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(
            self.corner, self.width, self.height)

    def __repr__(self):
        return "Rectangle({0}, {1}, {2})".format(
            repr(self.corner), self.width, self.height)

    def area(self):
        #return the area of any instance
        return self.width * self.height

    def perimeter(self):
        #return perimeter of any rectangle instance
        return (self.width + self.height)*2

    def flip(self):
        #swap the width and the height of any rectangle instace
        temp = self.width
        self.width = self.height
        self.height = temp

    def contains(self, Point):
        #test if a Point falls within the rectangle
        myX = self.corner.x
        myY = self.corner.y
        newX = Point.x
        newY = Point.y
        if(newX >= myX and newX < myX+self.width and newY >= myY and newY < myY+self.height):
            return True
        else:
            return False


    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

