

""" ocean levels """

# keep runing the loop for 25 iterations
for year in range(1,26) :
    
    yearly_raising_level = 1.6 # the yearl increasement level 
    
    ocean_level = year * yearly_raising_level  # calculate the ocean level each year until 25 years
    
    print(f'The ocean level in {year} year is {ocean_level:.2f}') ## display the ocean level each year until year 25
    
    