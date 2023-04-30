

""" Time Calculator """

def time_calculator(number_in_second) :
    
    # convert the number.
    
    second = number_in_second % (24 * 3600)
    hours  = second // 3600
    second %= 3600
    mintes =  second // 60 
    second %= 60 
    
    
    print(hours, ':', mintes, ':', second)

            
 

number_in_second = int(input('Enter the number of second ? ').strip())

print()
time_calculator(number_in_second)