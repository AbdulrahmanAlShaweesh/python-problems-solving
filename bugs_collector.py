

"""
Bug Collector
this program used to find the total number of bugs collected in a specfic days

 """



total_bugs = 0

number_of_days = int(input('Enter the number of days ? ').strip())

for day in range(1,number_of_days+1) :
    
    bug_collected = int(input(f'Enter the numbers of bugs collected in day {day} : ').strip())
    
    total_bugs += bug_collected 
    
print(f'The total bugs collected in {number_of_days} days is is {total_bugs} ')
