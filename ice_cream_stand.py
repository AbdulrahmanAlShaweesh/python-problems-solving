


class Restaurant :
    
    def __init__(self, restaurant_name, cusin_type) :
        
        self.restaurant_name = restaurant_name
        self.cusin_type  = cusin_type
        
    def describe_restaurant(self) :
        print(self.restaurant_name + ' Restaurant ' , end= ' ')
        print('serves an ' + self.cusin_type + ' cusines.')
    
    def open_restaurant(self) :
        print('The resturant is Opening...')

R = Restaurant('ardaljanatain', 'arabic')

R.open_restaurant()


class IceCreamStand(Restaurant): 
    
    def __init__(self, restaurant_name, cusin_type):
        self.flavor = ['choclate', 'strowbary', 'caffe', 'orange', 'mango']
        
        super().__init__(restaurant_name, cusin_type)
    
    def all_flavor(self) :
        
        for index, name in enumerate(self.flavor) :
            
            print(f'{index+1} : {name}')
            
ice_cream_1 = IceCreamStand('kfc', 'fast food')

ice_cream_1.all_flavor()
    
    