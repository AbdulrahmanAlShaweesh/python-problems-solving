

""" Sandwitch """


""" 

This Program used to create a function that accabte a list which containe as many as 
sandwitch toppings required, the parameter accebted as many as need of the toppings once
we call that function 

"""
def make_sandwitch(*sandwitch_toping) :
    
    for index, item in enumerate(sandwitch_toping) :
        
        print(str(index+1).zfill(2), ': ' , item.title(), 'added to your sandwitch'.title())

make_sandwitch('butter', 'bread', 'chips', 'cheese')
print('*******************************************')
make_sandwitch('tuna', 'vergtables', 'bread')
print('*******************************************')
make_sandwitch('bread', 'sausage', 'ransh souces', 'spicy', 'eggs', 'onine')