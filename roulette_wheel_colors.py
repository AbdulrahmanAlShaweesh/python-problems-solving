
""" Roulette Wheel Colors """

def roulette_wheel_colors(color_number) :
    
    if color_number == 0 : # return green color if color number 0
        
        return 'Pachage ' + str(color_number) + ' is green'
    
    elif color_number > 0 and color_number <= 36 : # execuit the following code if the color number in range of 0-36
        
         
        if color_number > 0 and color_number <= 10 :
            
            if color_number % 2  != 0 :
                
                return 'The package ' + str(color_number) + ' is red color'
            else :
                
                return 'The package ' + str(color_number) + ' is black colro'
            
        elif color_number >= 11 and color_number <= 18 :
            
            if color_number % 2 != 0 :
                
                return 'The package ' + str(color_number) + ' is black color'
            
            else :
                return 'The package ' + str(color_number) + ' is red color'
        
        elif color_number >= 19 and color_number <= 28 :
            
            if color_number % 2 != 0 :
                return 'The package ' + str(color_number) + ' is red color'
            
            else :
                return 'The package ' + str(color_number) + ' is black color'
        else :
            
            if color_number % 2 != 0 : 
                return 'The package ' + str(color_number) + ' is black color'
            else :
                return 'The package ' + str(color_number) + ' is red color.'
    else : # retunr error message if color number not in range of 0-36
        
        return 'Error, Color Number should be between 0-36.'

color_number = int(input('Enter the Color Number ? ').strip())

print(roulette_wheel_colors(color_number))
