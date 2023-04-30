

# Distance Traveled
# this program calculated the distance of a car trvels in mph

speed = int(input('What is the speed of the vehicle in mph(eg.120) ?').strip())
hours = int(input('How many hours has it traveled?').strip())


print('Hours\t\t\t\tDistance Traveled')
print('-------------------------------------')
for hour in range(1,hours+1) :
    distance = speed * hour    # calculate distance traveled
    
    print(f'{hour}\t\t\t\t\t\t{distance}') # display both hours and distance traveled
    
    