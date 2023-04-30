

def paint_job_estimator() :

    try :
        wall_space = float(input('Enter the space of wall need to be panted(squre feet) ? ').strip())
        paint_galon_price = float(input('Enter the price for the gallon of paint ? ').strip())

        number_of_paint_required = wall_space / 112          # number of paint need per gallow
        labor_hours_required = (wall_space / 112) * 8    # number of hours required to complet painting
        painting_cost  = paint_galon_price * number_of_paint_required # the total cost for painting
        labor_charge = labor_hours_required * 35           # charge for painting.
        total_cost_of_painting_job = painting_cost + labor_charge

        return f'The number gallon of paint required {number_of_paint_required}.', \
                  f'The number of hours required to finish painting {labor_hours_required}.', \
                      f'The total cost to pay the painting ${painting_cost}.', f'The total charge for painting {labor_charge}.', \
                        f'The total painting cost is {total_cost_of_painting_job}.'


    except ValueError as err:
        print(err)
    

paint_required, hours_required, paint_price, painting_charge, total_cost = paint_job_estimator()
print('-' * 50)
print(paint_required, hours_required,paint_price,painting_charge, total_cost, sep='\n')
       
        