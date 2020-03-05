from math import log, pi

temperature_water = 100    # °C
temperature_yolk = 70      # °C

kilograms_per_gram = 1/1000
mass = 47 * kilograms_per_gram   # kg (small egg)
mass = 67 * kilograms_per_gram   # kg (large egg)

centimeters_per_meter = 100
density = 1.038 * kilograms_per_gram * centimeters_per_meter**3    # kg m^-3

specific_heat_capacity = 3.7 / kilograms_per_gram                  # J kg^-1 K^-1
thermal_conductivity = 5.4e-3 * centimeters_per_meter              # W m^-1 K^-1


# from the refrigerator
temperature_original = 4   # °C (refrigerator)

prefactor = (mass**(2/3) * specific_heat_capacity * density**(1/3)) / \
            (thermal_conductivity * pi**2 * (4 * pi / 3)**(2/3))

argument = 0.76 * (temperature_original - temperature_water) / (temperature_yolk - temperature_water)

time = prefactor * log(argument)

print('From the refrigerator, time for yolk to reach {:.0f} °C  = {:.0f} s'.format(temperature_yolk, time))

# from room temperature
temperature_original = 20  # °C (room temperature)

prefactor = (mass**(2/3) * specific_heat_capacity * density**(1/3)) / \
            (thermal_conductivity * pi**2 * (4 * pi / 3)**(2/3))

argument = 0.76 * (temperature_original - temperature_water) / (temperature_yolk - temperature_water)

time = prefactor * log(argument)

print('From room temperature, time for yolk to reach {:.0f} °C  = {:.0f} s'.format(temperature_yolk, time))
