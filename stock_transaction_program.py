

""" 
Stock Transaction Program

"""

def stock_transaction_program(total_shares_purchse, purchase_price, purchase_commission,
                              total_shares_sold, sold_price, sold_commission) :
    total_amount_of_purchase = total_shares_purchse * purchase_price # total amount of money joe purchase
    total_purchase_commission = total_amount_of_purchase * purchase_commission # total purchase commission
    total_purchase_include_commission = total_amount_of_purchase + total_purchase_commission # total money he paid when he bought the shares
    
    ## this data caluclate the shares sold information.
    total_amount_of_sold = total_shares_sold * sold_price # calcuate the total money he sold the shares.
    total_sold_commissions = total_amount_of_sold * sold_commission # calculate the sold commission (3%)
    total_sold_include_commission = total_amount_of_sold + total_sold_commissions # total amount of money he made including the capital and commissions
    
    # joe profits.
    
    profit = total_sold_include_commission - total_purchase_include_commission
    
    if profit < 0 :
        
        print('The Total amount of money Joe Paid to stock when Purchased the shares is $' + str(total_amount_of_purchase))
        print('The Total Purchase Commission $' + str(total_purchase_commission))
        print('The Total Amount of money he paid inclding commission $', str(total_purchase_include_commission))
        print('The Total amount of money Joe REcived when sold the shares is $' + str(total_amount_of_sold))
        print('The Total sold Commission $' + str(total_sold_commissions))
        print('The Total Amount of money he Recived inclding commission ', str(total_sold_include_commission))
        print('Joe Losted a total amount of $' + str(profit)[1:])
    else :
        print('The Total amount of money Joe Paid to stock when Purchased the shares is $' + str(total_amount_of_purchase))
        print('The Total Purchase Commission $' + str(total_purchase_commission))
        print('The Total Amount of money he paid inclding commission $', str(total_purchase_include_commission))
        print('The Total amount of money Joe REcived when sold the shares is $' + str(total_amount_of_sold))
        print('The Total sold Commission $' + str(total_sold_commissions))
        print('The Total Amount of money he Recived inclding commission ', str(total_sold_include_commission))
        print('he Profit Joe Made $' + str(profit))
        
    
# purchase data.
total_shares_purchse = 2000
purchase_price = 40
purchase_commission = 0.03

# sold data.
total_shares_sold = 2000
sold_price = 38
sold_commission = 0.03

stock_transaction_program(total_shares_purchse, purchase_price, purchase_commission,
                            total_shares_sold, sold_price, sold_commission)
