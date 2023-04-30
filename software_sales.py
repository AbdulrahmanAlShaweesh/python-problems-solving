

""" . Software Sales """

def  software_sales(number_purchase, package_price) :
    
    if number_purchase > 0 :
        
        if number_purchase < 10 :
            price_before = number_purchase * package_price
            price_after  = price_before 
            discount = 0
            return  f'The total Price Beofre discount is ${price_before}\nThe total Price after discount is ${price_after}\ndicount is ${discount}'
        
        elif number_purchase >= 10 and number_purchase <= 19:
            price_before = number_purchase * package_price
            discount = (price_before * 0.1)
            price_after  =  price_before - discount 
            return  f'The total Price Beofre discount is ${price_before}\nThe total Price after discount is ${price_after}\ndicount is ${discount}'
        
        elif number_purchase >= 20 and number_purchase <= 49:
            price_before = number_purchase * package_price
            discount = (price_before * 0.2)
            price_after  =  price_before - discount 
            return  f'The total Price Beofre discount is ${price_before}\nThe total Price after discount is ${price_after}\ndicount is ${discount}'
            
        elif number_purchase >= 50 and number_purchase <= 99:
            price_before = number_purchase * package_price
            discount = (price_before * 0.3)
            price_after  =  price_before - discount 
            return  f'The total Price Beofre discount is ${price_before}\nThe total Price after discount is ${price_after}\ndicount is ${discount}'
        
        else:
            price_before = number_purchase * package_price
            discount = (price_before * 0.4)
            price_after  =  price_before - discount 
            return  f'The total Price Beofre discount is ${price_before}\nThe total Price after discount is ${price_after}\ndicount is ${discount}'

    else :
        return 'The number of packages should be 0 or higher.'
    
number_purchase = int( input('Enter the number of package you purchased ? ').strip() ) # number of package customer purchased
package_price = 99 

print(software_sales(number_purchase, package_price))