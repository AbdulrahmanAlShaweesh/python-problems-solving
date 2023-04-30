

# Average Rainfall
# this program calculated the average of ranfaill per month during a spefific number of years

try :
    
    years = int(input('Enter the number of years ? ').strip()) 
    
    total_rainfall = 0
    number_of_months = 0
    
    for year in range(1,years+1) :
        print() 
        print(f'---------------------------- Year {year} -------------------------------------')
        for month in range(1,13) :
            
            try :
                
                rainfail_in_inches = float(input(f'Enter the inches of rainfal for month{month}  ? ').strip()) 
                
                # total rainfal during 12 months
                total_rainfall += rainfail_in_inches 
                number_of_months += 1
            
            except :
                print('please enter invalid value for the months')
                
                
    print('============================================================================')
    print(f'The total number of the months {"are" if number_of_months > 1 else "is"} ' + str(number_of_months) )
    print(f'The total inches of rainfall is {total_rainfall}')
    print(F'The average inches of rainfall per months {"are" if (total_rainfall / number_of_months) else "is"}  {(total_rainfall / number_of_months)}')

except :
    print('please enter a valid value as a year')
    
