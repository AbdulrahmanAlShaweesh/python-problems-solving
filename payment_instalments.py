

""" payment Instalments """

def payment_instalements(user_purchases, desired_number_payment) :
    
    total_including_profit = (user_purchases * 0.05) + user_purchases
    amount_per_each_instalement = total_including_profit / desired_number_payment
    
    return total_including_profit, amount_per_each_instalement

user_total_purchases = float(input('Write the total amount you purchased ? ').strip())
instalements_number = float(input('Write the number of instalment you want ? ').strip())

total, instalement_amount = payment_instalements(user_total_purchases, instalements_number)
print('The total amount of money you need to pay is $' + str(total))
print('You need to pay $' + str(instalement_amount) + ' per each instalment') 

    