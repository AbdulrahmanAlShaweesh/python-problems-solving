

def grade_calculator(test_1, test_2, main_test) :
    
    total_points = test_1 + test_2 + main_test 
    
    if (test_1 >= 0 and test_1 <= 25) and (test_2 >= 0 and test_2 <= 25) and (main_test >= 0 and main_test <= 50):
        
        if main_test > 25 and total_points > 50 :
            
            if total_points > 80 and total_points <= 100 :
                return 'Your Grade is "Distinction"'
            
            elif total_points > 60 and total_points < 80 :
                return 'Your Grade is "Credit"'
            
            else :
                return 'Your Grade is "Pass"'
        
        else :
            if main_test < 25 :
                return 'Your main exam point is ' + str(main_test) + ' Sorry, You Faild in main exam'
            else :
                return 'Your total points are ' + str(total_points) + ' Sorry, You total points less than 50'
            
    else :
        
        
        if (test_1 < 0 or test_1 > 25) and (test_2 > 0 and test_2 < 25) and (main_test >= 0 and main_test <= 50):
            return 'error, test one points should be between 0-25'
        
        elif (test_1 > 0 and test_1 < 25) and (test_2 < 0 or test_2 > 25) and (main_test >= 0 and main_test <= 50):
            return 'error, test two points should be between 0-25'
        
        else :
            return 'error, main exam points should be between 0-25'

test_1_points = int(input('Enter Your First Text Points ? ').strip())
test_2_points = int(input('Enter Your Second Test Points ? ').strip())
main_exam_points = int(input('Enter Your Main Exam Points ? ').strip())

print(grade_calculator(test_1_points, test_2_points, main_exam_points))