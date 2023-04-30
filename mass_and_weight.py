
""" Mass and Weight """ 

def mass_and_weight(object_mass) :
    
    # calculate_weight in newton
    weight = object_mass * 9.8
    
    if weight > 500 :
        
        return f'weight is {weight:.2f} and it is to heavy'
    
    elif weight < 100 :
        
        return f'weight is {weight:.2f} and it is to light.'
    
    else :
    
        return f'weight is {weight:.2f} and it is normal.'

object_mass_in_kg = float(input('Write the object\'s mass in (KG) ? ').strip()) 

weight_in_newton = mass_and_weight(object_mass_in_kg)
print(weight_in_newton)

