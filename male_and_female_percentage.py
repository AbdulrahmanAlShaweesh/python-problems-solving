
""" 
Male and Female Percentage 

"""

def male_female_percentage(number_of_students, male_students, female_students) :
    
    """ Calculate and Return The Percentage of both male and female student in 
        the class
        """
    percentage_of_male_students = (male_students / number_of_students) * 100
    percentage_of_female_students = (female_students / number_of_students) * 100
    
    return percentage_of_male_students, percentage_of_female_students

number_of_students = int(input('Enter the Number of Male and Female Students? ').strip())
male_students = int(input('Enter the Number of Male Students? ').strip())
female_students = int(input('Enter the Number of Female Students? ').strip())

male, female = male_female_percentage(number_of_students, male_students, female_students)
print(f'Percentage of Male Students in the class {"is" if male_students == 1 else "are"} % {male}')
print(f'Percentage of Female Students in the class {"is" if female_students == 1 else "are"} % {female}')
