

""" Hot Dog Cookout Calculator """

def hot_dog_cookout_calculator(people_attempt, hot_dog_need, hot_dog_bout) :
    
    hot_dog_pachage = (people_attempt * hot_dog_need) / 10
    hot_dog_bount_package = (people_attempt * hot_dog_bout) / 8
    
    hot_dog_pachage_left_over = (people_attempt * hot_dog_need) % 10
    hot_dog_pachage_bount_left_over = (people_attempt * hot_dog_need) % 8 # 
    
    return hot_dog_pachage, hot_dog_bount_package, hot_dog_pachage_left_over, hot_dog_pachage_bount_left_over
    
    

people_attempt = int(input('Enter the number of people will attempt the cookout ? ').strip())
hot_dog_need = int(input('Enter the number of hot dog need for each one ? ').strip())
hot_dog_bout = int(input('Enter the number of hot dog bount need for each one ? ').strip())

print('The  Minimum Number of Pachage of Hot Dog required is ' + str(hot_dog_cookout_calculator(people_attempt, hot_dog_need, hot_dog_bout)[0]))
print('The  Minimum Number of Pachage of Hot Dog Bunts required is ' + str(hot_dog_cookout_calculator(people_attempt, hot_dog_need, hot_dog_bout)[1]))
print('The  Minimum Number of  of Hot Dog Will be Left ' + str(hot_dog_cookout_calculator(people_attempt, hot_dog_need, hot_dog_bout)[2]))
print('The  Minimum Number of  of Hot Dog Bunts Will be Left ' + str(hot_dog_cookout_calculator(people_attempt, hot_dog_need, hot_dog_bout)[3]))

 
