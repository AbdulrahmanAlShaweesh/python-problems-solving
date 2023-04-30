


def max_of_two_values(n1, n2) :

    if n1 > n2 :

        return f'{n1} is greater than {n2}.'

    elif n1 < n2 :

        return f'{n1} is less than {n2}.'

    else :

        return f'{n1} is equal to {n2}.'

try :

    number1 = int(input('Enter the first number ? ').strip() )
    number2 = int(input('Enter the second number ? ').strip() )

    if type(number1) != int :
        print('only intergers allowed')
    

except ValueError as err :

    print('only numberical data allowed.')

else :

    max_value = max_of_two_values(number1, number2)
    print(max_value)