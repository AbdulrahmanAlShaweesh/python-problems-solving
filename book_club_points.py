

""" Book Club Points """

def book_club_points(number_of_booked) :
    
    if number_of_booked >= 0 : # the following code will execuit only if the value is 0 or higher
        
        if number_of_booked == 0 : 
            return 'You got 0 points for this month.' 
        
        elif number_of_booked == 2 :
            return 'you got 5 points for this month'.capitalize()
    
        elif number_of_booked == 4 :
            return 'you got 15 points for this month'.capitalize()
        
        elif number_of_booked == 6 :
            return 'you got 30 points for this month'.capitalize()
        
        else : 
            return 'you got 60 points for this month'.capitalize()
    else : # return error message indecate the value is negative
        return 'Please enter a valid number (from 0 and up).'

# number of tick or book user made during the month
number_of_booked = int(input('Enter how many times you purchased this books club during this month ? ').strip())

print(book_club_points(number_of_booked))