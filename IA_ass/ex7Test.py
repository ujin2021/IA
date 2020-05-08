import ex7
import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

print("<Point class>")
test1 = ex7.Point(3,5)
test2 = ex7.Point(3,5)
test3 = ex7.Point(4,10)

print("---Test 1---")
print(test1 == test2) #True
print(test1 != test3) #True

print("---Test 2---")
print(test1.reflect_x()) #Point(3, -5)

print("---Test 3---")
print(test3.slope_from_origin()) #2.5
print(ex7.Point(0,0).slope_from_origin())
print(ex7.Point(0,4).slope_from_origin()) #Exception handling
print(ex7.Point(-3,-3).slope_from_origin())

print("---Test 4---")
print(ex7.Point(4, 11).get_line_to(ex7.Point(6, 15)))
print(ex7.Point(4, 11).get_line_to(ex7.Point(4,15))) #Exception handling
print(ex7.Point(4, 11).get_line_to(ex7.Point(3,11)))

print("\n<Rectangle class>")
print("---Test 1,2,3---")
r = ex7.Rectangle(ex7.Point(100, 50), 10, 5)
test(r.area() == 50)
test(r.perimeter() == 30)
r.flip()
test(r.width == 5 and r.height == 10)

print("---Test 4---")
r = ex7.Rectangle(ex7.Point(0, 0), 10, 5)
test(r.contains(ex7.Point(0, 0)))
test(r.contains(ex7.Point(3, 3)))
test(not r.contains(ex7.Point(3, 7)))
test(not r.contains(ex7.Point(3, 5)))
test(r.contains(ex7.Point(3, 4.99999)))
test(not r.contains(ex7.Point(-3, -3)))