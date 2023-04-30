


"""
Pounds to Kilograms convertion

"""
def Pounds_to_Kilograms(mass_object_in_pound, pound_unit) :
    
    """ calculate and return the mass object in kg"""
    weight_in_kg = float(mass_object_in_pound) * pound_unit 
    return f'Your weight in kg is {weight_in_kg:.2f} kg'

while True :
    
    print('enter "Q" to exit the calculator.')
    one_pound_in_kg = 0.454  ## value of one pound in kg
    mass = input('Enter your weight in pound(S)> ').strip() 
    if mass.lower() == 'q' :
        print('Thanks for using pound to kg convertion calculator')
        print('Good Bye...')
        break
    
    object_mass_in_kg = Pounds_to_Kilograms(mass, one_pound_in_kg)
    print(object_mass_in_kg)
    
