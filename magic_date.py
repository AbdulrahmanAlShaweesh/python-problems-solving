
""" check if the year entered by user is a magic year or not """

def magic_date(day, month, year) :
    
    month_times_day = day * month
    
    if month_times_day == year : # check if the month_times_day is equal to year, then reutrn date is a magic date
        return 'The Year ' + f'{month}/{day}/{year}' + ' is a magic Date.'
    else : # else will reutrn date is not a magic date
        return 'The data ' +  f'{month}/{day}/{year}' + ' is not a magic Date.'

day = int(input('Enter the day in numerical form (interger only? ').strip() )
month = int(input('Enter the month in numberical form (only integer) ? ').strip())
year = int(input('Enter the last two digits of the year (only integer) ? ').strip())

print(magic_date(day, month, year))
