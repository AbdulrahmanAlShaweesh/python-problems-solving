

""" Areas of Rectangles """


def areas_of_rectangles(rec1_width, rec1_length, rec2_width, rec2_length) : 
    
    rect_1_area = rec1_width * rec1_length
    rect_2_area = rec2_width * rec2_length
    
    if rect_1_area > rect_2_area :
        return f'The area of Rectangular 1 is {rect_1_area} and its greater than area of rectangular 2'
    elif  rect_1_area < rect_2_area:
        return f'The area of Rectangular 1 is {rect_1_area} and its smaller than area of rectangular 2'
    else :
        return 'area of both rectangulars are equals'
    
rec1_width = float(input('Enter the width of Rectangular 1 ? ').strip())
rec1_length = float(input('Enter the Length of Rectangular 1 ? ').strip())
rec2_width = float(input('Enter the width of Rectangular 2 ? ').strip())
rec2_length = float(input('Enter the Length of Rectangular 2 ? ').strip())

resu = areas_of_rectangles(rec1_width, rec1_length, rec2_width, rec2_length)
print(resu)

    
    