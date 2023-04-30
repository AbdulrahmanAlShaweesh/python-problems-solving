


print('Reboot the computer and try to connect.')
answer = input('id that fix the problem? ').strip()

if answer == 'no' :

    print('Reboot the computer and try to connect.')
    answer = input('id that fix the problem? ').strip()

    if answer == 'no' :

        print('Make sure the cables between the router & modem are plugged in !rmly.')
        answer = input('id that fix the problem? ').strip()

        if answer == 'no' :
            print('Move the router to a new location and try to connect.')
            answer = input('id that fix the problem? ').strip()

            if answer == 'no' :
                print('Get a New Router.')
            
            else :

                quit()
        
        else :
            quit() 


    else :
        quit()  

   

else : 
    quit()