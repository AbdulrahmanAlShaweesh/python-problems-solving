# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 15:46:03 2022

@author: abood
"""

""" 
annual profit => 23% => 023

"""

def company_annual_profit(annual_profit, total_sales) :
    """calculate and then return total profit"""
    total_profit = float(total_sales) * annual_profit
    return total_profit

while True :
    
    annual_profit = 0.23
    print('Welcome to the sales profit calculation')
    print('Enter "q" to exit.\n')
    
    total_sales = input('Write The Total Amount of Sales? ').strip()
    if total_sales.lower() == 'q' :
        print('Thanks For using our Program')
        print('Good Bye...')
        break
    t = company_annual_profit(annual_profit, total_sales)
    print(t)
        
