#The assignment is to make a program that will be used to calculate the roots of a quadratic equation and also state the minimum/ maximum values of the curve.

import math

def calculate_roots(a, b, c):
    #since the discriminant is used to know the kind and number of roots, we use it as a determining factor.
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        #if the discriminant is greater than zero, the roots are real and distinct
        root1 = (-b + (math.sqrt(discriminant))) / 2*a
        root2 = (-b - (math.sqrt(discriminant))) / 2*a
        return f"The roots are real and distinct: {root1}, {root2}"
    elif discriminant == 0:
        #if the discriminant is 0, the roots are real and equal
        root = -b / (2*a)
        return f"The roots are real and equal: {root}"
    else:
        #if the discriminant is less than zero then the roots are complex and distinct
        real_part = -b / (2*a)
        imaginary_part = (math.sqrt(-discriminant)) / 2*a
        return f"The roots are complex and distinct: {real_part} + {imaginary_part}i, {real_part} - {imaginary_part}i"
    
def find_vertex(a, b, c):
    # to find the x_vertex (x-coordinate of the curve)
    x_vertex = -b / (2*a)
    # to find the y_vertex (y-coordinate of the curve)
    y_vertex = (a * x_vertex**2) + (b * x_vertex) + c
    
    #to determine if it is maximum or minimum, we use the value of a becaus if a is positive, the vertex represents the minimum value but if it is negative, the vertex represnts a maximum value. a cannot be equal to zero.
    if a > 0:
        return f"and the minimum value is y = {y_vertex} at x = {x_vertex}"
    else:
        return f"and the maximum value is y = {y_vertex} at x = {x_vertex}"
    
a = float(input("Enter the coefficient of x**2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant: "))


print(calculate_roots(a, b, c), find_vertex(a, b, c))