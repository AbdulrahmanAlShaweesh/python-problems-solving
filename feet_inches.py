

# feet inches 

def feet_to_inches(n_feets) :

    value_in_inches = n_feets * 12      # convert feet to inches.

    return f'The {n_feets} feets is equal to {value_in_inches} in inches.' # return the feet value and inches values

try :

    number_feet = float(input('Enter the number of feets ? ').strip())  # feets values entered by user

except ValueError as err :
    print('only numberical input allowed!')  # exception error occurs if try not execuit

else :

    inches = feet_to_inches(number_feet)  # else will execuit if try execuits
    print(inches)

