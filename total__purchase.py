
"""
Total Purchage

"""

def total__purchase(item1_price, item2_price, item3_price, item4_price, item5_price) :
    
    total_purchases = float(item1_price) + float(item2_price) + \
                      float(item3_price) + float(item4_price) + float(item5_price)
    tax = total_purchases / 5
    total = total_purchases + tax
    
    return total_purchases, tax, total 

while True :
    print('Welcome to Total Purchase system')
    print('enter "q" to exit the system\n')
    item1 = input("Price of first Item? ").strip()
    if item1.lower() == 'q' :
        break
    
    item2 = input("Price of second Item? ").strip()
    if item2.lower() == 'q' :
        break
    item3 = input("Price of third Item? ").strip()
    if item3.lower() == 'q' :
        break
    item4 = input("Price of fourth Item? ").strip() 
    if item4.lower() == 'q' :
        break
    item5 = input("Price of fivth Item? ").strip()
    if item5.lower() == 'q' :
        break
    x, y, z = total__purchase(item1, item2, item3, item4, item5)
    print('----------------------------------------------')
    print("The total Purchase Salse ", x)
    print("The total purchase tax is ", y)
    print("The total amount of money is ", z)
    
    
    
    