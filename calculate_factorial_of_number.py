# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 08:10:36 2022

@author: abood
"""
total_factory_number = 1   # initionalize the total number

user_nonnegative_number = int(input('Enter a nononegatice number? ').strip()) # user number

for number in range(user_nonnegative_number, 0, -1) :
    total_factory_number *= number # calculated the factorial numbers

# display a message of the total factorial number user entered
print('The factorial number of ' + str(user_nonnegative_number) + ' is ' + str(total_factory_number))