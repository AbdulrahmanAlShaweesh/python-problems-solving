
""" 

making a pizza 

"""

def make_pizza(size, *toppings) :
    
    print('making ' + str(size) + '-inch pizza with the following toppings: ')
    
    for top in toppings :
        print('- ', top)
        
make_pizza(12, 'mushrooms', 'green papers', 'extra cheese' )