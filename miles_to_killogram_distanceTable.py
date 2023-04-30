

""" Miles to Kilometers Table """



try :
    
    distance_in_miles = int(input('Enter the values in miles ? ').strip()) # distance in miles
    
    print()
    
    print('distance in Miles\t\t\t\t\tdistance in KG') 
    print('-----------------------------------------------------')
    
    for i in range(10, distance_in_miles+1, 10) :   # conver the distance in mile into kg
        
        distance_in_kg = (i * 1.60934) 
        print(f'{i}\t\t\t\t\t\t\t\t\t\t{distance_in_kg:.2f}')
        
except :
    
    print('Pleae enter invalid value for the dsitance')