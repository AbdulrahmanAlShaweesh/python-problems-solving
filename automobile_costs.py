


# automobile costs .

"""  this fuction used to as the user for the automobile cost monthly and annual expenses of the folowing:
1 - car loan
2 - car insurance 
3 - car gas
4 - car oil
5 - tires
6 - mantainace
"""

def automobile_costs(car_loan, car_insurance, car_gas, car_oil, car_tires, car_mantainace) :

    total_monthly_cost = car_loan + car_insurance + car_gas + car_oil + car_tires + car_mantainace # calculate the monthly costs
    total_annual_cost = total_monthly_cost * 12                                                    # calculate the annual costs.

    return f'The total Monthly cost for the car is {total_monthly_cost:.2f}', \
                           f'The total annual cost of the car is {total_annual_cost:.2f}'    # return total monthly and yearly cost
                            
car_loan = float(input('Enter the monthly loan of the car ? ').strip())
car_insurance = float(input('Enter the monthly insurance for the car ? ').strip())
car_gas  = float(input('Enter the monthly cost of the car\'s gas ? $').strip())
car_oil  = float(input('Enter the car\'s monthly oil ? $').strip())
car_tires = float(input('Enter the car\'s monthy for tires ? $').strip())
car_mantainace = float(input('Enter the cost for mantiance the car monthly ? $').strip())

monthly_cost, annual_cost = automobile_costs(car_loan, car_insurance, car_gas, car_oil, car_tires, car_mantainace)
print(monthly_cost, annual_cost)
