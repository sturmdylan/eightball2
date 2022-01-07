# Uncomment this when you reach the "Use the Force" section
# train_mass = 22680
# train_acceleration = 10
# train_distance = 100
# bomb_mass = 1


# Write your code below:
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
print(f_to_c(100))


# f100_in_celsius = f_to_c input(100)

# Temp (F) = Temp (C) * (9/5) + 32

# print(c0_in_fahrenheit) = 32.0
def get_force(mass, acceleration):
  return mass * acceleration
print(get_force(5, 3))

print("The GE train supplies train_force Newtons of force")

def get_enegry(mass, c = 3*10**8):
  return mass*c**2
  bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies "+str(bomb_energy)+" Joules.")

def get_work(mass, acceleration, distance):
  return get_force*distance

print("The  GE train does train_work Joules of work over train_work meters. ")