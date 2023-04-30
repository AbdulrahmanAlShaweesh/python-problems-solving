

""" Restaurant """

class Restaurant :
    
    def __init__(self, restaurant_name, cuisine_type, time) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.time = time 
        
    def descripe_restaurant(self) :
        print('Restaurant Name ' + self.restaurant_name)
        print('Cuisine Type ' + self.cuisine_type)
        
    def open_restaurant(self) :
        
        print(f'{"The Restaurant is opening Now..." if self.time > 10 else "The Restaurant is Closed Now"}')
        
        
        
restaurant = Restaurant('Al_haramian', 'Arabic Dishes', 10)

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.descripe_restaurant()
restaurant.open_restaurant()