
""" Number of Customer that used to serve in """

class Resturant :
    
    def __init__(self, name, cuisine) :
        self.resturant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0
        
    def decribe_restuarant(self) : # display the information of the resturant
        return self.resturant_name + ' Restuarant is used to Served  an ' + self.cuisine_type + ' cuisines'
    
    def open_restuarant(self) : 
        
        return f'Restuarnat {self.resturant_name} is opening at 12 PM...'
    
    def customer_served_number(self) :
        return self.number_served
    
    def set_number_served(self, number_of_customer_served) :
        self.number_served = number_of_customer_served
    
    def increment_number_served(self,number) :
        self.number_served += number
        
restuarant_1 = Resturant('KFC', 'Arabic')
print(restuarant_1.resturant_name)
print(restuarant_1.cuisine_type)
print(restuarant_1.decribe_restuarant())
print(restuarant_1.open_restuarant())
print() 
print('The Restuarant Served a ' + str(restuarant_1.number_served) + ' Customer.')
restuarant_1.number_served = 100 # new number of customer the restuarant served
print('The Restuarant Served a ' + str(restuarant_1.customer_served_number()) + ' Customer.')
restuarant_1.set_number_served(900)
print('The Restuarant Served a ' + str(restuarant_1.customer_served_number()) + ' Customer.')
restuarant_1.increment_number_served(200) 
print('The Restuarant Served a ' + str(restuarant_1.customer_served_number()) + ' Customer.')
