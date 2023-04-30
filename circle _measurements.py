
import math  as m 
""" Circle Measurements"""

def circle_measurements(radius) :
    
    """Return and calculate the area of circle and area of circumference"""
    
    area_of_circle = m.pi*pow(radius,2)
    area_of_circumference = 2*(m.pi*radius)
    
    return area_of_circle, area_of_circumference

r = float(input('Enter the radius of a circle ? ').strip()) # radius of a circle


area, circumference_area = circle_measurements(r)
print(f'The area of the circle is {area:.2f}')
print(f'The area of circumference is {circumference_area:.2f}')
 
 