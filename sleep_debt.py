

total_slept_hours = 0            # initiolize the total sleeping hours user had
required_sleep_hours = (7 * 8)   # total sleep hours user should have during 7 days

# run the script for 7 days 
for day in range(1,8) :         
    
    # promot user to enter number of hour he/she slept in a spesific day
    sleeping_hours = float(input(f'Enter the nuber if hours you slept in day {day}? ').strip()) 
    
    total_slept_hours += sleeping_hours    # calculate the total hours he / she slept in each day
    
    # calculate the debt sleep
    print(total_slept_hours)

debt_sleep = total_slept_hours - required_sleep_hours

if (debt_sleep == 0) : # check if the user has not sleep debt will exiecut the folowing code
    print('WOW, you had a grate sleep this week')
    
else :
    
    if debt_sleep > 0:
        print('You have slept more than enough for this week')
        
    else :
        print('You have not slept enough this week')
