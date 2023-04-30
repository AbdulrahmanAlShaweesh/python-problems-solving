


# monthly sales tax 

def monthly_sales_tax() :

    try :

        monthly_totale_sales = float(input('Enter the total monthly sales ? $').strip())
    
    except ValueError as err :

        print('only numberical data allowed.')
    
    else :

        state_tax = (monthly_totale_sales * 0.05) 
        county_tax = (monthly_totale_sales * 0.025)
        total = (monthly_totale_sales + state_tax + county_tax) 
    return total ,state_tax, county_tax

total_sales, c_tax, s_tax = monthly_sales_tax() 

print('The total sales is $' + str(round(total_sales,2)))
print('The total state tax is $' + str(round(s_tax,2))) 
print('The total county tax is $' + str(round(c_tax,2))) 