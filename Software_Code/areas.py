import math

def Square(a):			     # square
  return a * a

def Rectangle(a, b):		 # rectangle
  return(a * b)

def Triangle(b, h):		     # triangle
  return(b * h / 2)

def Circle(r):			     # circle
  return(math.pi * r * r)

def Cylinder(r, h):		     # cylinder
  return(2 * math.pi * r * h)

print("AREAS OF SHAPES")
print("===============\n")
print("What is the shape?: ")

shape = input("Square (s)\nRectangle(r)\nCircle(c)\n\
Triangle(t)\nCylinder(y): ")

shape = shape.lower()
if shape == 's':
  a = float(input("Enter a side of the square: "))
  area = Square(a)
  s = "Square"
elif shape == 'r':
  a = float(input("Enter one side of the rectangle: "))
  b = float(input("Enter other side of the rectangle: "))
  area = Rectangle(a, b)
  s = "Rectangle"
elif shape == 'c':
  radius = float(input("Enter radius of the circle: "))
  area = Circle(radius)
  s = "Circle"
elif shape == 't':
  base = float(input("Enter base of the triangle: "))
  height = float(input("Enter height of the triangle: "))
  area = Triangle(base, height)
  s = "Triangle"
elif shape == 'y':
  radius = float(input("Enter radius of cylinder: "))
  height = float(input("Enter height of cylinder: "))
  area = Cylinder(radius, height)
  s = "Cylinder"

print("Area of %s is %f" %(s, area))


   


   
   




 



    

    
    

