

# Calories from Fat and Carbohydrates
# this program will calculate the number of coloreies that will be lost from 
# fat and carbs from daily consumed.

def colories_lost_from_fat_and_carbohydrat(fat, carbs) :
    try :
        
        colories_from_fat = fat * 9
        colories_from_carbohydrate = carbs * 4 

        return f'The colores will be lost from fat is {colories_from_fat}', \
                                f'The colories will be lost from carbs are {colories_from_carbohydrate}' 
    except ValueError:
        print('Value error, only numberical data allowed.')
try : 

    fat = float(input('Enter the number of fat you consumed in a day "per grams" ? ').strip())
    carbohydrate = float(input('Enter the number of carbohydrate you consumed in a day "in grams" ? ').strip())

    cor_fat, cor_carbs = colories_lost_from_fat_and_carbohydrat(fat, carbohydrate) 

except ValueError :
    print('can not enter empty value.')

else :
    print(cor_fat, cor_carbs, sep='\n')