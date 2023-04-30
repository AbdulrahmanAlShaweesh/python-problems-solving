

""" Body Mass Index=> BMI used to indecate a person's weight """


def body_mass_index(name, weight_in_kg, height) :
    
    # convert the weight into pound and height in inches.
    weight_in_pounds = weight_in_kg * 2.2046
    height_in_inchdes = height  * 39.37    # convert meter into inches.
    

    # calculate BMI. 
    BMI = weight_in_pounds * (703 / pow(height_in_inchdes, 2))
    
    if BMI > 0 :
        
        if BMI >= 18.5 and BMI <= 25 :
            return name + f' Your BMI is {BMI:.2f}' + ' Your weight is optimal'
        
        elif BMI < 18.5 :
            return name + f' Your BMI is {BMI:.2f}' + ' You are underweight.'
        
        else :
            
            return name + f' Your BMI is {BMI:.2f}'  + ' you are overweight.'
        
    else :
        return name + ' Sorry, Your BMI can not be less than 0.'

name = input('Enter Your Name ? ').strip()
weight_in_kg    = float(input('Enter Your Weight in kg ? ').strip())
height_in_meter = float(input('Enter Your height in meters ? ').strip())

print(body_mass_index(name, weight_in_kg, height_in_meter))
