



# Favorite Number

import json 

def promot_user_favourite_number() :

    try :

        fav_number = float(input('Write your favourit number ? ').strip())

    except ValueError :
        return 'Value error.'

    else :
        return fav_number 

def read_data() :

    number = promot_user_favourite_number() 

    try :

        with open('user_fav_number.txt', 'w') as file :

            json.dump(number, file) 
    
    except FileNotFoundError :

        return None 

    else :
        return number

def call_data() :

    data = read_data() 

    if data :

        print('Hello user, I knew You fav number is ' + str(data))
    


call_data()    
    

