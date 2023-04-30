
""" 
Planting Grapevines

"""

def planting_grapevines(length_of_row, amount_of_space, space) :
    
    number_of_grapevine_V = (length_of_row - (2 * amount_of_space)) / space
    
    return f'The Number of grapevines  That Will fit in Row {number_of_grapevine_V} '

length_of_row = float(input('Write the row in feet ? ').strip())
amount_of_space = float(input('Write the amount of space used by an end-post assemble, in feet? ').strip())
space = float(input('Write the spaces between vines in feets? ').strip())

resulte = planting_grapevines(length_of_row, amount_of_space, space)
print(resulte)
