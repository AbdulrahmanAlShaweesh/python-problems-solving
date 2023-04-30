

# return average scoor.
def  calc_averag(tests) :

    total = 0  
    for score in tests :
       
       total += int(score)# cal  tests average.

    return total / len(tests) 

test_1 = input('Enter the 5 test grade with space spriter ? ').split()   # promot user to enter tests grades
 

def determine_grade() :

    test_score = calc_averag(test_1)

    if (test_score < 0) or (test_score > 100) :
        return 'The score should be in range of 0-100'

    else :

        if (test_score > 0) and (test_score < 60) :

            return f'Your Score is {test_score}\nYour Grade is "F".'
        
        elif (test_score >= 60) and (test_score < 70) :
            return f'Your Score is {test_score}\nYour Grade is "D".'

        elif (test_score >= 70) and (test_score < 80) :
            return f'Your Score is {test_score}\nYour Grade is "C".'

        elif (test_score >= 80) and (test_score < 90) : 
            return f'Your Score is {test_score}\nYour Grade is "B".'

        else :

            return f'Your Score is {test_score}\nYour Grade is "A".' 

print(determine_grade())


