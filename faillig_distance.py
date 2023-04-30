

# failling distance 

def failling_distance(failling_time) :   # calculate the failling distance of the gravity effecting the object failling
    
     failling_distance_in_meter = 0.5 * 6.8 * failling_time ** 2

     return failling_distance_in_meter  # return the failling distance value


for i in range(10) :
 
    data = failling_distance(i)  # call the failling distacne function and each time pass the value i which will be from 0-9
    print(f'The Failling distance is {data:.2f}') # display the value on the screen.

