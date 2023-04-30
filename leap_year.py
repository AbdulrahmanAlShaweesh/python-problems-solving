

""" February Day """


# find if the year is a leap year or not.
def leap_year(year) :
    
    if (year % 4 == 0) and (year % 100 != 0) :
        print(f'In {year} February has 29 days')
    
    elif (year % 100 == 0)  and (year % 400 == 0)  :
        print(f'In {year} February has 29 days')
    else :
        print(f'In {year} February has 28 days')
        
for i in range(10) :
    
    year = int(input('Write the Year ? ').strip())
    
    leap_year(year)


 