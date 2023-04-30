


# Pennies for Pay 


 

working_days = int(input('Enter the number of days you worked ? ').strip() )

total_payments = 0

print('Day\t\t\t\t\t\t  Salary')
print('-----------------------------------------')


for day in range(1,working_days+1) :
    
    payments = 1 * 2 ** (day-1) 
    
    print(f'{day}\t\t\t\t\t\t\t${payments}')
    