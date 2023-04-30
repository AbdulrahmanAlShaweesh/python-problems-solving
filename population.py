
# Population 

start = 2 


print('Day Approximate\t\t\t\t\tPopulation')
for i in range(1,11) : # using loop to loop over 10 day
    
    if i == 1:
        increasement = 2
    else :
        increasement = start * 0.3
        start += increasement 
    print(f'\t{i}\t\t\t\t\t\t\t\t{start}.')
    
    