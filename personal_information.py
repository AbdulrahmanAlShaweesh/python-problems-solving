
""" this problem required to write 
name
address, city, state, zip code
phoneNumber
collage major
using input function
"""

def user_information(name, address, city, state, zipCode, phoneNumber, collageMajor) :
    print('Name => ' + name)
    print('Address => ' + address)
    print('City => ' + city)
    print('State => ' + state)
    print('Zip Code => ' + zipCode)
    print('Phone Number => ' + str(phoneNumber))
    print('Collage Major => ' + collageMajor)



name = input('Nmae > ').strip().lower()
address = input('Address => ')
city = input('City> ').strip().lower()
state = input('State > ').strip().lower()
zipeCode = input('Zip Code > ').strip().lower()
phoneNumber = input('Phone Number > ').strip()
collage_major = input('Collage Major > ').strip().lower()
user_information(name, address, city, state, zipeCode, int(phoneNumber), collage_major)

 