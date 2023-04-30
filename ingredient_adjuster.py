

""" .Ingredient Adjuster """ 

def ingredient_adjuster(cup_of_sugre, cup_of_butter, cup_of_flour, cooks, cookies) :
    
    sugre_need =  (cup_of_sugre * cooks) / cookies
    butter_need = (cup_of_butter * cooks) / cookies
    flour_need =  (cup_of_flour * cooks) / cookies
    
    return sugre_need, butter_need, flour_need
cup_of_sugre = 1.5
cup_of_butter = 1
cup_of_flour = 2.75 

cooks = int(input('Write the number of cookies you need to make ? ').strip())
cookies = 48

sugar, butter, flour = ingredient_adjuster(cup_of_sugre, cup_of_butter, cup_of_flour, cooks, cookies)
print(f'The Following the ingredient Need to make a {cooks} of {"cookies" if cooks > 1 else "Cooky"}')
print('************************************************')
print(f'Sugre : {sugar:.2f}', f'Butter : {butter:.2f}', f'Flour : {flour:.2f}', sep='\n')