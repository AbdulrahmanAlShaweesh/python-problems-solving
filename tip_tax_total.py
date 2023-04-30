
""" Tip, Tax and Total """

def tip_tax_total_calculator(food_price,tip_amount,tax_amount) :
    
    total_tax = (food_charge * tax_amount)
    total_tip = (food_charge * tip_amount) 
    total_bill = food_charge + total_tax + total_tip 
    return total_tax, total_tip, total_bill

food_charge = float(input('enter the food charge ? ').strip())
tip_percentage = 0.18
tax_percentage = 0.07

bill, tip, tax = tip_tax_total_calculator(food_charge, tip_percentage, tax_percentage) 
print('Hello Dear Customer Your bill detials as following:')
print('**********************************************')
print(f'Total tip ${tip:.2f}' + '\n' + f'Total tax ${tax:.2f}'  + '\n' + f'Total bill ${bill:.2f}' )