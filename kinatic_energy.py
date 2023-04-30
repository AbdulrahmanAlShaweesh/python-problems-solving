

def kinatic_energy(mass_object, mass_velocity) :

    KE = 0.5 * mass_object * pow(mass_velocity, 2)   # calculate the kinatic energy

    return KE # return kinatic energy value.


# Program. 
m_object = float(input('Enter the mass object in kg ? ').strip())
m_velocity = float(input('Enter the mass verlocity in m/s ? ').strip())

print(f'The kinatic energy is {kinatic_energy(m_object, m_velocity)}') 