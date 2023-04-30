

# Prime Numbers 

def is_prime_number(num) :

    for num in range(2,num+1):
        for i in range(2,num):
            if ( num % i==0 ):
                break
        else:
            print(num, end='  ')
try :

    number = int(input('Enter a number ? ').strip())

except ValueError :
    print('only integer number allowed.')

else :

    is_prime_number(number)

 