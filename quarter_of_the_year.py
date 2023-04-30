 
""" . Quarter of the Year """

def quarter_of_the_year(month) :
    
    if month >= 1 and month <= 12 :
        
        if month >= 1 and month <= 3 :
            return 'Month in the First Quarter of the year'
        elif month >= 4 and month <= 6 :
            return 'The Month in the Second Quarter of The Year'
        elif month >= 7 and month <= 9 :
            return 'The Month in the Third Qurter of the year'
        else :
            return 'The Month in the fourth qurter of the year.'
    else :
        return 'The Month Should be in range of 1-12'


for i in range(14) :
    month = int(input('Write the number of the month between 1-12 (in int numbers) ? ').strip())
    result = quarter_of_the_year(month)
    print(result)