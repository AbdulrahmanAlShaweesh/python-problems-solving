

# How Much Insurance?
# this function as the owner to enter the building cost if he or she needs to replace the building
# and the calculate the property cost to replace that building owners need to pay "note : they need to pay 80%"
# of the replacement cost.

from time import clock_settime


def building_insurance(replacement_cost_percentage, building_cost) :

    minPaymenet = building_cost * 0.8  # find the minimum replacement cost of the property 80%

    return f'The minimum payment owners should pay for the property is ${minPaymenet:.2f}'

replacement_cost_percentage = 0.8 
building_cost = float(input('Enter the replacement cost of the building ? $').strip() )

print(building_insurance(replacement_cost_percentage, building_cost))