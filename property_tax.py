
# 0.72 for each $100

def calculateTaxPriceForAssesmentProperty(actualPrice) :

    assement_property = actualPrice * 0.6                       # caculate the assesment value of the proeraty
    assememt_tax      = (assement_property / 100)  * 0.72       # tax value of the proerty where each 100 => 0.72 cents as a tax      
    
    return f'The assesment\'s value of the property is ${assement_property:.2f}', f'The tax value of the property if ${assememt_tax:.2f}'

actualPrice = float(input('Enter the actual Price of the property? '))
assement_price, tax_price = calculateTaxPriceForAssesmentProperty(actualPrice) 
print(assement_price, tax_price, sep='\n')

             

   