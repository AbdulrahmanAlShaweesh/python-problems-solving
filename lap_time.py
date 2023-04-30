


# Lap Times 

# this program used to ask the users about the number of time they have runed arround a Lap Times

time_run_around_racetrack = int(input('Enter the how many times you runed arround a racetrack(eg. 5) ? ').strip())

all_round_time = [] 

for number in range(1,time_run_around_racetrack+1) :
    
    time_taken = float(input(f'Enter the number of mintes take you to finish round {number}.? ').strip())

    all_round_time.append(time_taken)
    
print(f'the fastest lap took {max(all_round_time)} Mintues')
print(f'the slowest lap took {min(all_round_time)} Mintues')
print(f'the average lap time is {sum(all_round_time) / len(all_round_time)} Mintues')
 