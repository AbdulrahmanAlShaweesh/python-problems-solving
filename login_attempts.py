 
""" Login Attempts """

class User :
    
    def __init__(self, userName, userAge) :
        self.username = userName
        self.userage = userAge 
        self.number_of_attempt  = 0
        
    def increase_number_of_attempt(self) :
        
        self.number_of_attempt += 1
    
    def reset_login_attempts(self) :
        self.number_of_attempt = 0
        
        
        
    