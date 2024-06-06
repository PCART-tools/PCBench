from sympy.geometry import Point3D, Line3D
point1 = Point3D(1, 2, 3)
point2 = Point3D(4, 5, 6)
line = Line3D(point1, point2)
equation = line.equation('x', y='y')
