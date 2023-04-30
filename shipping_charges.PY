

""" Shipping Charges """

def shipping_charges(package_weight) :
    
    if package_weight < 0 : # if package weight is less than 0 error message will indecate.
        print('The package\'s weight should be greater than 0')
    
    else :
        
        if package_weight <= 2 and package_weight > 0 :
            print('The shipping Rate is $1.5' )
        
        elif package_weight > 2 and package_weight <= 6 :
            print('The shipping Rate is $3.0' )
        
        elif package_weight > 6 and package_weight <= 10 :
            print('The shipping Rate is $4.0' )
        
        else :
            print('The shipping Rate is $4.75' )


# package weight in pound ( entered by user )
package_weight = float(input('Write the package weight in pund unit ? ').strip())
    
shipping_charges(package_weight)