
"""  miles_per_galon """

def miles_per_galon(mDriven, gasUsed) :
    MPG = mDriven / gasUsed
    return f'You Drived {MPG} Gallon of Gas Per {"Miles" if mDriven > 1 else Miles}'

mile_driven = float(input('Write The Number of Miles You Drive ? ').strip())
gallon_gas_used = float(input('Write The Number of Gallon of Gas used ? ').strip())

mpg = miles_per_galon(mile_driven, gallon_gas_used)
print(mpg)