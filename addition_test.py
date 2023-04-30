

import random

def addition_test() :

    for questionNumber in range(1,6) :

        print(f'Question {questionNumber}')
        num1 = random.randint(1,6)
        num2 = random.randint(1,6) 
        print(f'The sum of {num1} + {num2} => {num1 + num2}')
        print()

addition_test()