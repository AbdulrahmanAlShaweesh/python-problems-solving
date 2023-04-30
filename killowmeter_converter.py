

# Kilometer Converter
# this program ask user for the distance in killowmeter and then convert it to miles.


def kilometer_converter(distance_in_kilometer) :
    
    distance_in_miles = distance_in_kilometer * 0.6214

    return f'The distance in miles is {distance_in_miles:.2f}', f'The distance in kilometer is {distance_in_kilometer:.2f}'

distance_in_kilometer = float(input('enter the distance in kilometer ? ').strip())

miles_distance, kilometer_distance = kilometer_converter(distance_in_kilometer)
print(miles_distance, kilometer_distance, sep='\n')
