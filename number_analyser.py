
""" Number Analyser """

def number_analyser(number) :
    
    if number > 0 :
        if number % 2 == 0 :
            print('The Number You Entered is an Even Posstive Number')
        else :
            print('The Number You Entered is an Old Posstive Number')
            
    elif number < 0 :
        if number % 2 == 0 :
            print('The Number You Entered is an Even Negative Number')
        else :
            print('The Number You Entered is an Old Negative Number')
    else :
        print('The Number You Entered is a Zero')

num = int(input('Write an interger number ? ').strip())

number_analyser(num)