#1. Write a function that uses two arguments.

def format_example(number, char):
    result = "The number is: {} and the character is: '{}'".format(number, char)
    return result

formatted_string = format_example(145, 'o')
print(formatted_string)


#2. Calculate the area of the pond.

radius = 84
pi = 3.14
water_per_sqm = 1.4

area = pi * (radius ** 2)

total_water = area * water_per_sqm

print("Total water in the pond:", int(total_water), "liters")


#3. Calculate speed in meters per second

distance = 490  # in meters
time_minutes = 7
time_seconds = time_minutes * 60

speed = distance / time_seconds

print("Speed is", int(speed), "meters per second")