

""" Roman Numerals """

def roman_numerals(number) :
    
    if number >= 1 and number <= 10 :
        
        if number == 1 :
            number = 'I'
        elif number == 2 :
            number = 'II'
        elif number == 3 :
            number = 'III'
        elif number == 4 :
            number = 'IV'
        elif number == 5 :
            number = 'V'
        elif number == 6 :
            number = 'VI'
        elif number == 7 :
            number = 'VII'
        elif number == 8 :
            number = 'IIIV'
        elif number == 9 :
            number = 'IX'
        else :
            number = 'X'
        return number
    else :
        
        return f'error, {number} is not in range of 1-10'

for i in range(12) :    
    num = int(input('Write a number in range of 1-10? ').strip())
    
    roman_number = roman_numerals(num)
    if num > 10 :
        print(roman_number)
        
    else :
        
        print('Number\t\t\tRoman Number')
        print(f'  {num}\t\t\t\t\t  {roman_number}')