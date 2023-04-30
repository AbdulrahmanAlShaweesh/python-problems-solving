

import random 

def odd_even_counter(random_numbers) :
    odd_number = []
    even_number = []

    for number in random_numbers :
        if (number % 2) == 0 :
            odd_number.append(number) 

        else :
            even_number.append(number)

    return f'There {"are" if len(odd_number) > 1 else "is"} {len(odd_number)} odd numbers generated.', \
               f'There {"are" if len(even_number) > 1 else "is"} {len(even_number)} odd numbers generated.'

ra_numbers = [random.randint(0,100) for number in range(100)]  
print('**************************************************') 
print(odd_even_counter(ra_numbers))    
print(ra_numbers)
print('**************************************************') 
