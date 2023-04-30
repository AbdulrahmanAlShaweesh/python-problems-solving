

""" 
Compound Interest

"""

def compound_interest(orginal_deposit_amount, annual_interset, 
                      number_of_time_per_year, number_of_years) :
    
    A = orginal_deposit_amount * (1 + (annual_interset / number_of_time_per_year) ) ** \
                                                    (number_of_time_per_year * number_of_years)
    
    return f'the amount of money that will be in the account after the specified number of years {A:.2f}'

orginal_deposit_amount = float(input('Enter the Orginal deposited into the account? ').strip())
annual_interset = float(input('The annual interest rate paid by the account? ').strip())
number_of_time_per_year = float(input('''The number of times per year that the interest is compounded \
                                    (For example, if interest is compounded monthly, enter 12. \
                                     If interest is compounded quarterly, enter 4.)? ''').strip())
                                    
number_of_years = float(input('Write The number of years the account will be left to earn interest ? ').strip())
comInterset = compound_interest(orginal_deposit_amount, annual_interset, number_of_time_per_year, 
                                number_of_years)
print(comInterset)