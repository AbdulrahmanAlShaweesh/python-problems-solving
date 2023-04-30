

""" Money Counting Game """ 

def money_counting_game(pennies, nickles, dimes, quarter) :
    
    # calculate the total of money
    total_money = ((pennies * 1) + (nickles * 5) + (dimes * 10) + (quarter * 25)) / 100
    
    if total_money == 1 : # will return a congrates messsage is total money is exactly one dollor
        return 'Congrats, You Won the Game!'
    
    else : # else conditon will execuit if the total money is less or higher than one dollor
    
        if total_money > 1 : # return a message indecte that the money is greater than $1
            return 'The money is grater than $1.'
        
        else :# return a message indecte that the money is less than $1
            'The money is less than $1.'


# number of conis user had
pennies = float(input('Enter the number of pennies You have ? ').strip()) 
nickles = float(input('Enter the number of nickles You have ? ').strip()) 
dimes   =   float(input('Enter the number of dimes You have ? ').strip())
quarter = float(input('Enter the number of quarters You have ? ').strip())


print( money_counting_game(pennies, nickles, dimes, quarter) )