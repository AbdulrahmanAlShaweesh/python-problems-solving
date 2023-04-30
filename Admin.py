

class Users :
    
    def __init__(self, first_name, last_name, age, country) :
        
        self.fName = first_name
        self.lName = last_name
        self.age   = age
        self.country = country
        
    def describe_user(self) :
        
        print(f'user name ' + (self.fName.capitalize() + self.lName.capitalize()))
        print(f'user age ' + str(self.age)) 
        print(f'user country ' + self.country.capitalize())
        
    def called_greet_user(self) :
        
        print(f'Hello {self.fName + self.lName}')


user_1 = Users('abdulrahman', ' Ibraheem', 25, 'yemen')
user_1.describe_user()
user_1.called_greet_user()

class Admin(Users) :
    
   def __init__(self, first_name, last_name, age, country) :
       
       self.privileges = ['"can add post', 'can delete post', "can ban user"]
       
       super().__init__(first_name, last_name, age, country) 
       
   def show_privileges(self) :
        
        for i in self.privileges :
            print(i)
            
admin_1 = Admin('Abdulrahman', 'Ibraheem', 25, 'Yemen')

admin_1.show_privileges()
        
       
       
       
       