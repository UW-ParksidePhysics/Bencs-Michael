from math import pi

# constants
density_of_air = 1.2  # kg m^-3
mass = 0.43  # kg
acceleration_due_to_gravity = 9.81  # m s^-2
drag_coefficient = 1.2
gravity_force = mass * acceleration_due_to_gravity
print('Gravitational force is: {:.2f} N'.format(gravity_force))
radius = 0.11  # m
area_of_a_ball = pi * radius ** 2

meters_per_kilometer = 1000
seconds_per_hour = 60 * 60

#   hard kick
velocity = 120  # km/hr
velocity = velocity * meters_per_kilometer / seconds_per_hour  # m/s
drag_force = (1/2) * drag_coefficient * density_of_air (v* area_of_a_ball * velocity**2
print('Drag force on hard kick of v = {:.2f} is: {:.2f} N'.formatelocity, drag_force))


#   soft kick
velocity = 10  # km/hr
velocity = velocity * meters_per_kilometer / seconds_per_hour  # m/s
drag_force = (1/2) * drag_coefficient * density_of_air * area_of_a_ball * velocity**2
print('Drag force on soft kick of v = {:.2f} is: {:.2f} N'.format(velocity, drag_force))