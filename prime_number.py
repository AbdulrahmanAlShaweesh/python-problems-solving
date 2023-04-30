

# Prime Numbers 

def is_prime_number(num) :

     
    for number in range(2,num) :

        if num % number == 0 :
            print('it is not a prime number.')
    else :
        print('it is a prime number')

try :

    number = int(input('Enter a number ? ').strip())

except ValueError :
    print('only integer number allowed.')

else :
    is_prime_number(number)