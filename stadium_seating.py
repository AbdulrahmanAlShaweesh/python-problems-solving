

# this program used to calculate the total income for all 
# 3 class seats A,B C after entering the number of tickets sold 
# for each class 

def stadium_seats() :
    print('Wecome to ticket price calculator.')
    print('Class A ticket Price $20.\nClass B ticket Price $15.\nClass C ticket Price is $10.\n\n')
    
    try :
        class_A_tickets_number = int( input('Enter the number of tickets that sold from class A ? ').strip()) 
        class_B_tickets_number = int( input('Enter the number of tickets that sold from class B ? ').strip())
        class_C_tickets_number = int( input('Enter the number of tickets that sold from class C ? ').strip())
        
        total_price_A = class_A_tickets_number * 20
        total_price_B = class_B_tickets_number * 15
        total_price_C = class_C_tickets_number * 10

        total_income = total_price_A + total_price_B + total_price_C
        return f'Seat class A total ${total_price_A}.', f'TSeat class B total ${total_price_B}.', \
                                 f'Seat class C total ${total_price_C}.', f'The total incomde ${total_income}.'
    
    except ValueError as err:
        print(err)
    
classA, classB, classC,totalIncomes = stadium_seats() 
print(classA, classB, classC, totalIncomes, sep='\n')



